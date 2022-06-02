from itertools import chain

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

from login.exceptions import ObjectDeleted, MissingSalesContact
from login.models import User, Employee, Customer
from .models import Prospect, Provider, Contract, Event
from login.permissions import (ProspectPerm, ProviderPerm, ContractPerm,
                               EventPerm, CustomerPerm,
                               EmployeePerm, ValidToken, IsManager)
from . import serializers as appserializers
from . import filters


class SalesManagementSerializerAdapter:
    """ Adapt the serializer based on the status of the employee """

    sales_prospect_creation_serializer_class = None
    management_prospect_creation_serializer_class = None
    management_detail_serializer_class = None
    sales_detail_serializer_class = None
    
    def get_serializer_class(self):
        
        if 'create' in self.action:
            if self.request.user.status == 'SALES':
                return self.sales_prospect_creation_serializer_class
            return self.management_prospect_creation_serializer_class
        if self.request.user.status == 'SALES':
            return self.sales_detail_serializer_class
        return self.management_detail_serializer_class


class EventSerializerAdapter:
    """ Adapt the serializer based on the status of the user """

    event_customer_serializer = None
    event_employee_serializer = None

    def get_serializer_class(self):
        
        if self.request.user.status == 'CUSTOMER' and self.event_customer_serializer is not None:
            return self.event_customer_serializer
        return self.event_employee_serializer
    

class ContractSerializerAdapter:
    """
    Adapt the serializer used for the contract management based on the type of user, the action type, and the number of signature in the contract.
    
    In list mode :
        - For the user, return the default serializer
        - For the employee, return 'sales_list_serializer_class'

    In detailed mode : 
        For the employee : 
            - If there is no signature yet return the 'sales_serializer_class'
            - If there is one of the two signature return the 'sales_half_signed_employee_pov'
        For the customer
            - If there is no signature yet return the default serializer class
            - If there is one of the two signature return the 'sales_half_signed_customer_pov'
        If the contract is signed (two signature) return the 'sales_signed_contract_serializer_class'
        
    """

    sales_serializer_class = None
    sales_list_serializer_class = None
    sales_half_signed_employee_pov = None
    sales_half_signed_customer_pov = None
    sales_signed_contract_serializer_class = None
    
    def get_serializer_class(self):

        if 'pk' in self.kwargs:
            try:
                contract_obj = Contract.objects.get(id=self.kwargs['pk'])
            except ObjectDoesNotExist:
                return self.sales_serializer_class

            if self.request.user.status != 'CUSTOMER' and contract_obj.signed == True:
                return self.sales_signed_contract_serializer_class
            if self.request.user.status == 'CUSTOMER' and (contract_obj.customer_signature or contract_obj.employee_signature)  == True:
                return self.sales_half_signed_customer_pov
            if self.request.user.status != 'CUSTOMER' and (contract_obj.customer_signature or contract_obj.employee_signature) == True:
                return self.sales_half_signed_employee_pov
            
        if self.request.user.status != 'CUSTOMER' and self.action == 'create':
            return self.sales_list_serializer_class
        if self.request.user.status != 'CUSTOMER' and self.action != 'create':
            return self.sales_serializer_class

        return super().get_serializer_class()


@permission_classes([IsAuthenticated, ValidToken, EmployeePerm])
class EmployeeViewSet(ModelViewSet):
    """ Return the Employees objects attached to the manager """
    
    serializer_class = appserializers.EmployeeSerializer
    http_method_names = ['get', 'head', 'put', 'delete']
    filterset_class = filters.EmployeeFilter

    def get_queryset(self):

        user_connected = self.request.user.id

        managed_employees = Employee.objects.filter(manager=user_connected)
        
        return managed_employees


@permission_classes([IsAuthenticated, ValidToken, CustomerPerm])
class CustomerViewSet(ModelViewSet):
    """
    Return the Customers objects linked to their mission : 

    - For the MANAGER : Customers attached to the Employee he manage.
    - For the SUPPORT : Customers attached to the Event he manage.
    - For the SALES : Customers that have him as the FK 'Sales_contact'.
    
    """

    serializer_class = appserializers.CustomerSerializer
    http_method_names = ['get', 'head', 'put', 'delete']
    filterset_class = filters.CustomerFilter

    def get_queryset(self):

        user_connected = self.request.user.id
        user_status = User.objects.get(id=user_connected).status

        if user_status == 'MANAGER':
            managed_employees = Employee.objects.filter(manager=user_connected)
            customers_objects = [Customer.objects.filter(sales_contact=managed_employee.id) for managed_employee in managed_employees]
            chain_customers = list(chain(*customers_objects))
            customers_ids = [customer.id for customer in chain_customers]
            customers_qs = Customer.objects.filter(id__in=customers_ids)
            
        if user_status == 'SUPPORT':
            events = Event.objects.filter(support_id=user_connected)
            customers_ids = set([event.customer_id.id for event in events])
            customers_qs = Customer.objects.filter(id__in=customers_ids)
            
        if user_status == 'SALES':
            customers_qs = Customer.objects.filter(sales_contact=user_connected)
            
        return customers_qs
    

@permission_classes([IsAuthenticated, ValidToken, ProspectPerm])
class ProspectViewSet(SalesManagementSerializerAdapter, ModelViewSet):
    """ Return Prospect objects associated to the Sales-Employee or the Manager-Employee """
    
    
    sales_detail_serializer_class = appserializers.SalesProspectSerializer
    management_detail_serializer_class = appserializers.ManagementProspectSerializer
    sales_prospect_creation_serializer_class = appserializers.SalesProspectCreationSerializer
    management_prospect_creation_serializer_class = appserializers.ManagementProspectCreationSerializer
    
    filterset_class = filters.ProspectFilter

    def get_queryset(self, *args, **kwargs):

        user_connected = self.request.user.id  
        user_status = User.objects.get(id=user_connected).status
                
        if user_status == 'SALES':
            prospect_qs = Prospect.objects.filter(sales_contact=user_connected)

        if user_status == 'MANAGER':
            managed_employee = Employee.objects.filter(manager=user_connected)
            prospects_attached = [Prospect.objects.filter(sales_contact=employee) for employee in managed_employee]
            chain_prospects = list(chain(*prospects_attached))
            prospect_ids = [prospect.id for prospect in chain_prospects]
            prospect_qs = Prospect.objects.filter(id__in=prospect_ids)  

        return prospect_qs

    def get_object(self):
        prospect_obj = get_object_or_404(Prospect, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, prospect_obj)

        data_dict = self.request.data

        if self.request.method == 'PUT' and 'converted' in data_dict:

            if data_dict['converted'] == 'true':

                create_user_from_prospect(data_dict)
                
                prospect_obj.delete()

                raise ObjectDeleted      
            
        return prospect_obj
    
    def perform_create(self, serializer):
                
        if self.request.user.status == 'SALES':
            serializer.save(sales_contact=Employee.objects.get(id=self.request.user.id))
        else:
            serializer.save()

            
    
@permission_classes([IsAuthenticated, ValidToken, IsManager])
class FreeProspectViewSet(ModelViewSet):
    """ Return the prospect that has not been assigned for the moment. """
    
    serializer_class = appserializers.ManagementProspectSerializer
    filterset_class = filters.ProspectFilter

    def get_queryset(self):
        
        free_prospect_qs = Prospect.objects.filter(sales_contact=None) 
        
        return free_prospect_qs
    
    def get_object(self):

        prospect_obj = get_object_or_404(Prospect, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, prospect_obj)
        
        data_dict = self.request.data

        if self.request.method == 'PUT' and 'converted' in data_dict:
            if data_dict['converted'] == 'true':
                if not data_dict['sales_contact']:
                    raise MissingSalesContact

                create_user_from_prospect(data_dict)
                
                prospect_obj.delete()

                raise ObjectDeleted      
            
        return prospect_obj


@permission_classes([IsAuthenticated, ValidToken, ProviderPerm])
class ProviderViewSet(ModelViewSet):
    """ Return Provider objects if the user is an Employee """
    
    serializer_class = appserializers.ProviderSerializer
    filterset_class = filters.ProviderFilter

    def get_queryset(self):

        return Provider.objects.all()


@permission_classes([IsAuthenticated, ValidToken, ContractPerm])
class ContractViewSet(ContractSerializerAdapter, ModelViewSet):
    """ 
    Return the Contracts objects linked to their users : 
    
    - For the SALES : Contracts that have him as direct a referee with the FK='sales_contact'.
    - For the CUSTOMER : Contracts that the CUSTOMER his linked with.
    - For the SUPPORT : Contracts that are linked to the Events the SUPPORT user managed.
    - For the MANAGER : Contracts associated with the Employees he managed.

    """
    
    serializer_class = appserializers.CustomerContractSerializer
    sales_serializer_class = appserializers.EmployeeContractSerializer
    sales_list_serializer_class = appserializers.EmployeeCreationContractSerializer
    sales_half_signed_employee_pov = appserializers.ContractHalfSignedEmployeePOV
    sales_half_signed_customer_pov = appserializers.ContractHalfSignedCustomerPOV
    sales_signed_contract_serializer_class = appserializers.EmployeeSignedContractSerializer
    
    filterset_class = filters.ContractFilter
    
    def get_queryset(self):
        
        user_connected = self.request.user.id
        user_status = User.objects.get(id=user_connected).status
        
        if user_status == 'SALES':
            contract_qs = Contract.objects.filter(sales_contact=user_connected)
        if user_status == 'CUSTOMER':
            contract_qs = Contract.objects.filter(customer_id=user_connected)
        if user_status == 'SUPPORT':
            event_managed = Event.objects.filter(support_id=user_connected)
            event_ids = [event.contract_id.id for event in event_managed ]
            contract_qs = Contract.objects.filter(id__in=event_ids)
        if user_status == 'MANAGER':
            managed_employees = Employee.objects.filter(manager=user_connected)
            
            # Getting the contract linked to the SALES Employees the user Manage.
            contracts_queryset = [Contract.objects.filter(sales_contact=managed_employee.id) for managed_employee in managed_employees]
            chain_contracts = list(chain(*contracts_queryset))
            contracts_ids = [contract.id for contract in chain_contracts]
            
            # Getting the contract linked to the event of the SUPPORT Employees the user Manage.
            events_queryset = [Event.objects.filter(support_id=managed_employee.id) for managed_employee in managed_employees]
            chain_events = list(chain(*events_queryset))
            contracts_ids_from_event = [event.contract_id.id for event in chain_events]
            
            contracts_ids.extend(contracts_ids_from_event)  
                               
            contract_qs = Contract.objects.filter(id__in=contracts_ids)  
                  
        return contract_qs

    def get_object(self):
        
        contract_obj = get_object_or_404(Contract, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, contract_obj)
        
        signed = False
        
        if self.request.method == 'PUT':
            if 'customer_signature' in list(self.request.data):
                if contract_obj.employee_signature == True:
                    contract_obj.customer_signature = True
                    signed = True
            elif 'employee_signature' in list(self.request.data):
                if contract_obj.customer_signature == True:
                    contract_obj.employee_signature = True
                    signed = True
            if signed == True:
                contract_obj.signed = True
                contract_obj.save()
                if len(Event.objects.filter(contract_id=contract_obj.id)) == 0:
                    new_event = Event.objects.create(name=contract_obj.title, 
                                        contract_id=Contract.objects.get(id=contract_obj.id),
                                        customer_id=contract_obj.customer_id)

        return contract_obj


@permission_classes([IsAuthenticated, ValidToken, EventPerm])
class EventViewSet(EventSerializerAdapter, ModelViewSet):
    """ 
    Return the Event objects linked to their users : 
    
    - For the SALES : Events linked to the contracts he is referred to.
    - For the CUSTOMER : Events that the CUSTOMER his linked with.
    - For the SUPPORT : Events referring to him, FK='support_id'
    - For the MANAGER : Events associated with the Employees he managed.

    """

    event_customer_serializer = appserializers.EventCustomerPOV
    event_employee_serializer = appserializers.EventEmployeePOV
    
    filterset_class = filters.EventFilter

    def get_queryset(self):

        user_connected = self.request.user.id
        user_status = User.objects.get(id=user_connected).status

        if user_status == 'SALES':
            attached_contracts = Contract.objects.filter(sales_contact=user_connected)
            event_ids = [Event.objects.get(contract_id=contract_ref.id).id for contract_ref in attached_contracts]
            selected_events = Event.objects.filter(id__in=event_ids)
        if user_status == 'CUSTOMER':
            selected_events = Event.objects.filter(customer_id=user_connected)
        if user_status == 'SUPPORT':
            selected_events = Event.objects.filter(support_id=user_connected)
        if user_status == 'MANAGER':
            managed_employees = [Employee.objects.filter(manager=user_connected)][0]
            
            # Getting the event linked to the SUPPORT employees the user Manage.
            selected_events = [Event.objects.filter(support_id=employee.id) for employee in managed_employees]
            chained_events = list(chain(*selected_events))
            events_ids = [contract.id for contract in chained_events]
            
            # Getting the event linked to the contract of the SALES employees the user Manage.
            contracts_queryset = [Contract.objects.filter(sales_contact=managed_employee.id) for managed_employee in managed_employees]
            chain_contracts = list(chain(*contracts_queryset))
            contracts_ids = [contract.id for contract in chain_contracts]
            event_linked_contract = [event.id for event in Event.objects.filter(contract_id__in=contracts_ids)]
            
            events_ids.extend(event_linked_contract)

            selected_events = Event.objects.filter(id__in=events_ids) 


        return selected_events


@permission_classes([IsAuthenticated, ValidToken, IsManager])
class NotAssignedEventViewSet(EventSerializerAdapter, ModelViewSet):
    """ Return to the Managers the event that has be assign to a support Employee """
    
    event_employee_serializer = appserializers.EventEmployeePOV
    filterset_class = filters.EventFilter

    def get_queryset(self):

        not_assign_events = Event.objects.filter(support_id=None)
        
        return not_assign_events


@permission_classes([IsAuthenticated, ValidToken, IsManager])
class NotAssignedEmployeeViewSet(ModelViewSet):
    """ Return employees that do not have a manager, excluding the manager """
    
    serializer_class = appserializers.EmployeeSerializer

    def get_queryset(self):
        
        employee_qs = Employee.objects.filter(manager=None).filter(~Q(status='MANAGER'))
        
        return employee_qs


def create_user_from_prospect(data_dict):
    """ Create a user from a dict """
    
    new_user = Customer.objects.create(company_name=data_dict['company_name'],
                                        username=str(data_dict['first_name'])+str(data_dict['last_name']),
                                        first_name=data_dict['first_name'],
                                        last_name=data_dict['first_name'],
                                        email=data_dict['email'],
                                        phone_number=data_dict['phone_number'],
                                        sales_contact=Employee.objects.get(id=data_dict['sales_contact']),
                                        status='CUSTOMER')
    if len(data_dict['last_contact']) != 0:
        new_user.last_contact = data_dict['last_contact']
    new_user.set_password('password-oc')
    new_user.save()
