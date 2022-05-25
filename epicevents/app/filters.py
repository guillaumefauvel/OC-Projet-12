from django_filters import rest_framework as filters
from .models import Event, Contract, Provider, Prospect
from login.models import Customer, Employee


class EventFilter(filters.FilterSet):
    
    class Meta:
        model = Event
        fields = {
            'name': ['icontains'],
            'customer_id': ['exact'],
            'due_date': ['gte', 'lte'],
        }

class ContractFilter(filters.FilterSet):
    
    class Meta:
        model = Contract
        fields = {
            'title': ['icontains'],
            'customer_id': ['exact'],
            'sales_contact': ['exact'],
            'price': ['gte', 'lte'],
            'payed': ['exact'],
            'signed': ['exact']
        }
        
class ProviderFilter(filters.FilterSet):
    
    class Meta:
        model = Provider
        fields = {
            'type': ['exact'],
        }
        
        
class ProspectFilter(filters.FilterSet):
    
    class Meta:
        model = Prospect
        fields = {
            'company_name': ['icontains'],
            'sales_contact': ['exact'],
            'last_contact': ['gte', 'lte'],
        }
        
class CustomerFilter(filters.FilterSet):
    
    class Meta:
        model = Customer
        fields = {
            'username': ['icontains'],
            'sales_contact': ['exact']
        }
        
class EmployeeFilter(filters.FilterSet):
    
    class Meta:
        model = Employee
        fields = {
            'username': ['icontains'],
            'status': ['exact'],
        }
        
