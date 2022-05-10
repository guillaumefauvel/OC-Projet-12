from rest_framework.serializers import ModelSerializer

from .models import Prospect, Provider, Contract, Event
from login.models import User


class CustomerSerializer(ModelSerializer):

    class Meta:
        model = User
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
                  'last_contact',]


class ProviderSerializer(ModelSerializer):

    class Meta:
        model = Provider
        fields = ['id', 
                  'company_name',
                  'email',
                  'phone_number']
    

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
            'signed',
            'creation_date',
            'modified_date'
            ]

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