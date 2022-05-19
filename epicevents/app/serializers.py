from datetime import date

from rest_framework.serializers import ModelSerializer, ChoiceField, SerializerMethodField

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
                  'last_contact', 
                  'sales_contact']
        read_only_fields = ['sales_contact']


class EmployeeSerializer(ModelSerializer):
      
    events = SerializerMethodField()
    contracts = SerializerMethodField()
    prospects = SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 
                  'username',
                  'status',
                  'first_name',
                  'last_name',
                  'phone_number',
                  'events',
                  'contracts', 
                  'prospects']


    def get_events(self, instance):

        events = Event.objects.filter(support_id=instance.id).filter(due_date__lte=date.today().strftime("%Y-%m-%d"))
        serializer = EventSerializerSynthetic(events, many=True)
        return serializer.data

    def get_contracts(self, instance):
        
        contracts = Contract.objects.filter(sales_contact=instance.id).filter(signed=False)
        serializer = ContractSerializerSynthetic(contracts, many=True)
        return serializer.data

    def get_prospects(self, instance):
        
        contracts = Prospect.objects.filter(sales_contact=instance.id)
        serializer = ProspectSerializerSynthetic(contracts, many=True)
        return serializer.data


class SalesProspectSerializer(ModelSerializer):

    class Meta:
        model = Prospect
        fields = ['id', 
                  'company_name',
                  'email',
                  'first_name',
                  'last_name',
                  'phone_number',
                  'sales_contact',
                  'creation_date',
                  'modified_date',
                  'last_contact', 
                  'converted']
        read_only_fields = ['sales_contact']
        
        
class ManagementProspectSerializer(ModelSerializer):

    class Meta:
        model = Prospect
        fields = ['id', 
                  'company_name',
                  'first_name',
                  'last_name',
                  'email',
                  'phone_number',
                  'sales_contact',
                  'creation_date',
                  'modified_date',
                  'last_contact', 
                  'converted']


class ProviderSerializer(ModelSerializer):
    
    type = ChoiceField(choices=Provider.PROVIDER_TYPE)

    class Meta:
        model = Provider
        fields = ['id', 
                  'company_name',
                  'email',
                  'phone_number', 
                  'type']
    

class EmployeeContractSerializer(ModelSerializer):
    
    class Meta:
        model = Contract
        fields = [
            'id', 
            'title',
            'customer_id',
            'sales_contact',
            'price',
            'payed',
            'amount_payed',
            'contract_infos',
            'employee_signature',
            'customer_signature',
            'signed',
            'creation_date',
            'modified_date']
        
        read_only_fields = ['signed', 'customer_signature', 'customer_id', 'sales_contact']


class EmployeeCreationContractSerializer(ModelSerializer):
    
    class Meta:
        model = Contract
        fields = [
            'id', 
            'title',
            'customer_id',
            'sales_contact',
            'price',
            'payed',
            'amount_payed',
            'contract_infos',
            'employee_signature',
            'customer_signature',
            'signed',
            'creation_date',
            'modified_date']
        
        read_only_fields = ['customer_signature', 'signed']


class CustomerContractSerializer(ModelSerializer):
    
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
            'modified_date']
        
        read_only_fields = ['signed', 'employee_signature', 'price', 'payed',
                            'amount_payed', 'customer_id', 'title']

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
        
    
class EventSerializerSynthetic(ModelSerializer):
    
    class Meta:
        model = Event
        fields = [
            'id', 
            'name',
            'contract_id',
            'customer_id',
            'due_date',
            ]
        

class ContractSerializerSynthetic(ModelSerializer):
    
    class Meta:
        model = Contract
        fields = [
            'id', 
            'title',
            'customer_id',
            'payed',
            'employee_signature',
            'customer_signature',
            'signed']


class ProspectSerializerSynthetic(ModelSerializer):

    class Meta:
        model = Prospect
        fields = ['id', 
                  'company_name',
                  'last_contact']


class EmployeeSignedContractSerializer(ModelSerializer):
    
    class Meta:
        model = Contract
        fields = [
            'id', 
            'title',
            'customer_id',
            'sales_contact',
            'price',
            'payed',
            'amount_payed',
            'contract_infos',
            'employee_signature',
            'customer_signature',
            'signed',
            'creation_date',
            'modified_date']
        
        read_only_fields = ['title', 'customer_id', 'sales_contact', 'price', 
                            'contract_infos', 'employee_signature', 'customer_signature',
                            'signed', 'creation_date', 'modified_date']
        

class ContractHalfSignedCustomerPOV(ModelSerializer):
    
    class Meta:
        model = Contract
        fields = '__all__'
    
        read_only_fields = ['title', 'customer_id', 'sales_contact', 'price', 
                            'payed', 'amount_payed', 'contract_infos', 'employee_signature',
                            'signed', 'creation_date', 'modified_date']

class ContractHalfSignedEmployeePOV(ModelSerializer):
    
    class Meta:
        model = Contract
        fields = '__all__'
    
        read_only_fields = ['title', 'customer_id', 'sales_contact', 'price', 
                            'contract_infos', 'customer_signature',
                            'signed', 'creation_date', 'modified_date']