from datetime import date

from rest_framework.serializers import ModelSerializer, ChoiceField, SerializerMethodField

from .models import Prospect, Provider, Contract, Event
from login.models import Customer, Employee


class CustomerSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id', 
                  'company_name',
                  'email',
                  'username',
                  'first_name',
                  'last_name',
                  'phone_number',
                  'sales_contact']

        read_only_fields = ['sales_contact']


class CustomerSynthetic(ModelSerializer):
    
    class Meta:
        model = Customer
        fields = ['id', 
                  'company_name',
                  'email',
                  'first_name',
                  'last_name',
                  'phone_number']


class EmployeeSyntheticSerializer(ModelSerializer):
    
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'phone_number']


class EmployeeSerializer(ModelSerializer):
      
    events = SerializerMethodField()
    contracts = SerializerMethodField()
    prospects = SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['id', 
                  'username',
                  'manager',
                  'email',
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
        
        prospects = Prospect.objects.filter(sales_contact=instance.id)
        serializer = ProspectSerializerSynthetic(prospects, many=True)
        return serializer.data
    
    
class ProviderSerializer(ModelSerializer):
    
    type = ChoiceField(choices=Provider.PROVIDER_TYPE)

    class Meta:
        model = Provider
        fields = ['id', 
                  'company_name',
                  'email',
                  'phone_number', 
                  'type']


# ---------------------
# PROSPECTS SERIALIZERS
# ---------------------

class ProspectSerializerSynthetic(ModelSerializer):

    class Meta:
        model = Prospect
        fields = ['id', 
                  'company_name',
                  'last_contact']


class SalesProspectSerializer(ModelSerializer):

    class Meta:
        model = Prospect
        fields = '__all__'

        read_only_fields = ['sales_contact']


class SalesProspectCreationSerializer(ModelSerializer):

    class Meta:
        model = Prospect
        fields = '__all__'

        read_only_fields = ['sales_contact', 'converted']
        

class ManagementProspectSerializer(ModelSerializer):

    class Meta:
        model = Prospect
        fields = '__all__'


class ManagementProspectCreationSerializer(ModelSerializer):

    class Meta:
        model = Prospect
        fields = '__all__'

        read_only_fields = ['converted']


# ---------------------
# EVENTS SERIALIZERS
# ---------------------


class EventCustomerPOV(ModelSerializer):
    
    support_id = SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'
    
    def get_support_id(self, instance):
        
        if instance.support_id:
            referee = Employee.objects.get(id=instance.support_id.id)
            serializer = EmployeeSyntheticSerializer(referee)
            return serializer.data
        return None


class EventEmployeePOV(ModelSerializer):
    
    customer_id = SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'
    
    def get_customer_id(self, instance):

        customer = Customer.objects.get(id=instance.customer_id.id)
        serializer = CustomerSynthetic(customer)
        return serializer.data


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


# ---------------------
# CONTRACTS SERIALIZERS
# ---------------------

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
    
    sales_contact = SerializerMethodField()
    
    class Meta:
        model = Contract
        fields = '__all__'
    
        read_only_fields = ['title', 'customer_id', 'sales_contact', 'price', 
                            'payed', 'amount_payed', 'contract_infos', 'employee_signature',
                            'signed', 'creation_date', 'modified_date']

    def get_sales_contact(self, instance):
        
        referee = Employee.objects.get(id=instance.sales_contact.id)
        serializer = EmployeeSyntheticSerializer(referee)
        return serializer.data
    
    
class ContractHalfSignedEmployeePOV(ModelSerializer):
    
    class Meta:
        model = Contract
        fields = '__all__'
    
        read_only_fields = ['title', 'customer_id', 'sales_contact', 'price', 
                            'contract_infos', 'customer_signature',
                            'signed', 'creation_date', 'modified_date']
        

class CustomerContractSerializer(ModelSerializer):
    
    sales_contact = SerializerMethodField()

    class Meta:
        model = Contract
        fields = '__all__'
        
        read_only_fields = ['signed', 'employee_signature', 'price', 'payed',
                            'amount_payed', 'customer_id', 'title', 'sales_contact']

    def get_sales_contact(self, instance):
        
        referee = Employee.objects.get(id=instance.sales_contact.id)
        serializer = EmployeeSyntheticSerializer(referee)
        return serializer.data
    
class EmployeeContractSerializer(ModelSerializer):
    
    class Meta:
        model = Contract
        fields = '__all__'
        
        read_only_fields = ['signed', 'customer_signature', 'customer_id', 'sales_contact']


class EmployeeCreationContractSerializer(ModelSerializer):
    
    class Meta:
        model = Contract
        fields = '__all__'

        read_only_fields = ['customer_signature', 'signed']