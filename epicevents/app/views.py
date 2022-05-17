from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes

from login.models import User, Employee, Customer
from .models import Prospect, Provider, Contract, Event
from .serializers import (CustomerSerializer,
                          EmployeeSerializer,
                          SalesProspectSerializer,
                          ManagementProspectSerializer,
                          EmployeeCreationContractSerializer,
                          ProviderSerializer,
                          EmployeeContractSerializer,
                          CustomerContractSerializer,
                          EventSerializer)
from login.permissions import ProspectPerm, ProviderPerm, ContractPerm, EventPerm, CustomerListPerm, FreeEventPerm


class SalesManagementSerializerAdapter:

    management_serializer_class = None

    def get_serializer_class(self):

        if User.objects.get(id=self.request.user.id).status != 'SALES' and self.management_serializer_class is not None:
            return self.management_serializer_class

        return super().get_serializer_class()


class ContractSerializerAdapter:
    """
    Adapt the serializer used for the contract management based on the type of user and based on the action type.
    
    - For the user, return the default serializer
    - For the Employee, return the sales_serializer_class if he is on the retrieve view
    - For the Employee, return the sales_list_serializer_class if he is on the list view
    
    """

    sales_serializer_class = None
    sales_list_serializer_class = None

    def get_serializer_class(self):
                
        if self.request.user.status != 'CUSTOMER' and self.sales_list_serializer_class is not None and self.action == 'create':
            return self.sales_list_serializer_class
        if self.request.user.status != 'CUSTOMER' and self.sales_serializer_class is not None and self.action != 'create':
            return self.sales_serializer_class

        return super().get_serializer_class()


class EmployeeViewSet(ModelViewSet):
    """ Return the Employees objects attached to the manager """
    
    serializer_class = EmployeeSerializer
    http_method_names = ['get', 'head', 'put', 'delete']

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

    serializer_class = CustomerSerializer
    http_method_names = ['get', 'head', 'put', 'delete']

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
    
    serializer_class = SalesProspectSerializer
    management_serializer_class = ManagementProspectSerializer
    
    def get_queryset(self):

        user_connected = self.request.user.id  
        user_status = User.objects.get(id=user_connected).status

        if user_status == 'SALES':
            prospects_attached = Prospect.objects.filter(sales_contact=user_connected)
            return prospects_attached
        if user_status == 'MANAGER':
            managed_employee = Employee.objects.filter(manager=user_connected)
            prospects_attached = [Prospect.objects.filter(sales_contact=employee) for employee in managed_employee][0]
            return prospects_attached
        
        return []
    

@permission_classes([ProspectPerm])
class FreeProspectViewSet(ModelViewSet):
    
    serializer_class = ManagementProspectSerializer
    
    def get_queryset(self):
        
        user_connected = self.request.user.id
        user_status = User.objects.get(id=user_connected).status
        
        if user_status == 'MANAGER':
            
            free_prospect = Prospect.objects.filter(sales_contact=None) 
            
            return free_prospect
        

@permission_classes([ProviderPerm])
class ProviderViewSet(ModelViewSet):
    """ Return Provider objects if the user is an Employee """
    
    serializer_class = ProviderSerializer

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
    - For the MANAGER : Contracts associated with the Employees he managed (Only SALES employees for the moment #TODO).

    """
    serializer_class = CustomerContractSerializer
    sales_serializer_class = EmployeeContractSerializer
    sales_list_serializer_class = EmployeeCreationContractSerializer

    filterset_fields = ['sales_contact']
    
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


@permission_classes([EventPerm])
class EventViewSet(ModelViewSet):
    """ 
    Return the Event objects linked to their users : 
    
    - For the SALES : Events linked to the contracts he is referred to.
    - For the CUSTOMER : Events that the CUSTOMER his linked with.
    - For the SUPPORT : Events referring to him, FK='support_id'
    - For the MANAGER : Events associated with the Employees he managed (Only Support employees for the moment #TODO).

    """
    
    serializer_class = EventSerializer

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
    
    serializer_class = EventSerializer
    http_method_names = ['get', 'head', 'put', 'delete']

    def get_queryset(self):

        user_connected = self.request.user.id
        user_status = User.objects.get(id=user_connected).status
        
        if user_status == 'MANAGER':
            
            not_assign_events = Event.objects.filter(support_id=None)
            
            return not_assign_events

        return []
    

class RecapViewset(ModelViewSet):
    
    pass