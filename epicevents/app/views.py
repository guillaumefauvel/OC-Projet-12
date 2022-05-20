from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes

from login.models import User, Employee, Customer
from .models import Prospect, Provider, Contract, Event
from login.permissions import ProspectPerm, ProviderPerm, ContractPerm, EventPerm, CustomerListPerm, FreeEventPerm, EmployeePerm
from . import serializers as appserializers
from . import filters

class SalesManagementSerializerAdapter:

    management_serializer_class = None

    def get_serializer_class(self):

        if User.objects.get(id=self.request.user.id).status != 'SALES' and self.management_serializer_class is not None:
            return self.management_serializer_class

        return super().get_serializer_class()


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
            contract_obj = Contract.objects.get(id=self.kwargs['pk'])

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


@permission_classes([EmployeePerm])
class EmployeeViewSet(ModelViewSet):
    """ Return the Employees objects attached to the manager """
    
    serializer_class = appserializers.EmployeeSerializer
    http_method_names = ['get', 'head', 'put', 'delete']
    filterset_class = filters.EmployeeFilter

    def get_queryset(self):

        user_connected = self.request.user.id
        user_status = User.objects.get(id=user_connected).status

        if user_status == 'MANAGER':
            managed_employees = Employee.objects.filter(manager=user_connected)
            return managed_employees

        return []


@permission_classes([CustomerListPerm])
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
            customers = [Customer.objects.filter(sales_contact=managed_employee.id) for managed_employee in managed_employees][0]
            return customers
        if user_status == 'SUPPORT':
            events = Event.objects.filter(support_id=user_connected)
            customers = [event.customer_id for event in events]
            return set(customers)
        if user_status == 'SALES':
            customers = Customer.objects.filter(sales_contact=user_connected)
            return customers
            
        return []


@permission_classes([ProspectPerm])
class ProspectViewSet(SalesManagementSerializerAdapter, ModelViewSet):
    """ Return Prospect objects associated to the Sales-Employee or the Manager-Employee """
    
    serializer_class = appserializers.SalesProspectSerializer
    management_serializer_class = appserializers.ManagementProspectSerializer
    filterset_class = filters.ProspectFilter

    def get_queryset(self, *args, **kwargs):

        user_connected = self.request.user.id  
        user_status = User.objects.get(id=user_connected).status
                
        if user_status == 'SALES':
            prospects_attached = Prospect.objects.filter(sales_contact=user_connected)
            return prospects_attached
        if user_status == 'MANAGER':
            managed_employee = Employee.objects.filter(manager=user_connected)
            prospects_attached = [Prospect.objects.filter(sales_contact=employee) for employee in managed_employee]
            if len(prospects_attached) > 0:
                prospects_attached = prospects_attached[0]
            return prospects_attached
                
        return []
    
    def get_object(self):
       
        prospect_obj = Prospect.objects.get(id=self.kwargs['pk'])

        if self.request.method == 'PUT':
            data_dict = self.request.data

            if 'converted' in list(self.request.data):
                print('yes')
            
            try:
                if data_dict['converted'] == 'true':
                    
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
                    
                    prospect_object = Prospect.objects.get(email=data_dict['email'])        
                    prospect_object.delete()
                    
                    return 
            except KeyError:
                pass
    
        return prospect_obj
    
@permission_classes([ProspectPerm])
class FreeProspectViewSet(ModelViewSet):
    
    serializer_class = appserializers.ManagementProspectSerializer
    filterset_class = filters.ProspectFilter

    def get_queryset(self):
        
        user_connected = self.request.user.id
        user_status = User.objects.get(id=user_connected).status
        
        if user_status == 'MANAGER':
            
            free_prospect = Prospect.objects.filter(sales_contact=None) 
            
            return free_prospect


@permission_classes([ProviderPerm])
class ProviderViewSet(ModelViewSet):
    """ Return Provider objects if the user is an Employee """
    
    serializer_class = appserializers.ProviderSerializer
    filterset_class = filters.ProviderFilter
    
    def get_queryset(self):

        user_connected = self.request.user.id
        verify_employee = Employee.objects.filter(id=user_connected)
        
        if len(verify_employee) != 0:
            return Provider.objects.all()
        
        return []


@permission_classes([ContractPerm])
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
            contracts_obj = Contract.objects.filter(sales_contact=user_connected)
        if user_status == 'CUSTOMER':
            contracts_obj = Contract.objects.filter(customer_id=user_connected)
        if user_status == 'SUPPORT':
            event_managed = Event.objects.filter(support_id=user_connected)
            contracts_obj = [event.contract_id for event in event_managed ]
        if user_status == 'MANAGER':
            managed_employees = Employee.objects.filter(manager=user_connected)
            contracts_obj = [Contract.objects.filter(sales_contact=managed_employee.id) for managed_employee in managed_employees][0]
        
        return contracts_obj

    def get_object(self):
        
        contract_obj = Contract.objects.get(id=self.kwargs['pk'])
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


@permission_classes([EventPerm])
class EventViewSet(ModelViewSet):
    """ 
    Return the Event objects linked to their users : 
    
    - For the SALES : Events linked to the contracts he is referred to.
    - For the CUSTOMER : Events that the CUSTOMER his linked with.
    - For the SUPPORT : Events referring to him, FK='support_id'
    - For the MANAGER : Events associated with the Employees he managed.

    """
    
    serializer_class = appserializers.EventSerializer
    filterset_class = filters.EventFilter


    def get_queryset(self):

        user_connected = self.request.user.id
        user_status = User.objects.get(id=user_connected).status

        if user_status == 'SALES':
            attached_contracts = Contract.objects.filter(sales_contact=user_connected)
            selected_events = [Event.objects.get(contract_id=contract_ref.id) for contract_ref in attached_contracts]
        if user_status == 'CUSTOMER':
            selected_events = Event.objects.filter(customer_id=user_connected)
        if user_status == 'SUPPORT':
            selected_events = Event.objects.filter(support_id=user_connected)
        if user_status == 'MANAGER':
            managed_employees = [Employee.objects.filter(manager=user_connected)][0]
            selected_events = [Event.objects.filter(support_id=employee.id) for employee in managed_employees][0]
            
        return selected_events


@permission_classes([FreeEventPerm])
class NotAssignedEventViewSet(ModelViewSet):
    """ Return to the Managers the event that has be assign to a support Employee """
    
    serializer_class = appserializers.EventSerializer
    filterset_class = filters.EventFilter

    def get_queryset(self):

        user_connected = self.request.user.id
        user_status = User.objects.get(id=user_connected).status
        
        if user_status == 'MANAGER':
            
            not_assign_events = Event.objects.filter(support_id=None)
            
            return not_assign_events

        return []
    

