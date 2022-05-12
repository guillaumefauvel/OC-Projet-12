from rest_framework.serializers import ModelSerializer, ChoiceField

from .models import Prospect, Provider, Contract, Event
from login.models import User, Customer, Employee


class CustomerSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id', 
                  'company_name',
                  'first_name',
                  'last_name',
                  'phone_number',
                  'creation_date',
                  'modified_date',
                  'last_contact']


class EmployeeSerializer(ModelSerializer):
    
    # TODO - ADD contracts/events/prospects/customers
    
    class Meta:
        model = User
        fields = ['id', 
                  'status',
                  'first_name',
                  'last_name',
                  'phone_number',
                  'creation_date',
                  'modified_date',]


class ProspectSerializer(ModelSerializer):
    
    class Meta:
        model = Prospect
        fields = ['id', 
                  'company_name',
                  'email',
                  'phone_number',
                  'creation_date',
                  'modified_date',
                  'last_contact']


class ProviderSerializer(ModelSerializer):
    
    type = ChoiceField(choices=Provider.PROVIDER_TYPE)

    class Meta:
        model = Provider
        fields = ['id', 
                  'company_name',
                  'email',
                  'phone_number', 
                  'type']
    

class ContractSerializer(ModelSerializer):
    
    class Meta:
        model = Contract
        fields = [
            'id', 
            'title',
            'customer_id',
            'price',
            'payed',
            'amount_payed',
            'contract_infos',
            'employee_signature',
            'customer_signature',
            'signed',
            'creation_date',
            'modified_date',
            'history']
        
        read_only_fields = ['signed', 'history']

class EventSerializer(ModelSerializer):
    
    class Meta:
        model = Event
        fields = [
            'id', 
            'name',
            'description',
            'program',
            'contract_id',
            'support_id',
            'customer_id',
            'due_date',
            'creation_date',
            'modified_date',
            'providers'
            ]