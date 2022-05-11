from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets

from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin
)

from login.models import User, Employee, Customer
from .models import Prospect, Provider, Contract, Event
from .serializers import (CustomerSerializer,
                          EmployeeSerializer,
                          ProspectSerializer,
                          ProviderSerializer,
                          ContractSerializer,
                          EventSerializer,
                          )


class EmployeeViewSet(RetrieveModelMixin, ListModelMixin, viewsets.GenericViewSet):
    
    serializer_class = EmployeeSerializer

    def get_queryset(self):

        user_connected = self.request.user.id
        user_status = User.objects.get(id=user_connected).status

        # TODO - Voir pour implémenter cet élément là avec un décorateur
        if user_status == 'MANAGER':
            managed_employees = Employee.objects.filter(manager=user_connected)
            return managed_employees

        return []


class CustomerViewSet(RetrieveModelMixin, ListModelMixin, viewsets.GenericViewSet):
    
        
    serializer_class = CustomerSerializer

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
    

class ProspectViewSet(ModelViewSet):
    
    serializer_class = ProspectSerializer

    def get_queryset(self):

        return Prospect.objects.all()
    
    
class ProviderViewSet(ModelViewSet):
    
    serializer_class = ProviderSerializer

    def get_queryset(self):

        return Provider.objects.all()
    
    
class ContractViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, viewsets.GenericViewSet):
    
    serializer_class = ContractSerializer

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
            print(contracts_obj)
            return contracts_obj
        if user_status == 'MANAGER':
            managed_employees = Employee.objects.filter(manager=user_connected)
            contracts_obj = [Contract.objects.filter(sales_contact=managed_employee.id) for managed_employee in managed_employees]
            return contracts_obj[0]

        return []

    def get_object(self):

        urls_elements = [v for v in str(self.request).split('/') if v.isnumeric()]

        contributor_user = Contract.objects.get(id=urls_elements[0])

        return contributor_user


class EventViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, viewsets.GenericViewSet):
    
    serializer_class = EventSerializer

    def get_queryset(self):

        return Event.objects.all()