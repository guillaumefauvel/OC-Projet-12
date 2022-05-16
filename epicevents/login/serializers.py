from django.db.models import Q
from rest_framework import serializers
from django.contrib.auth import login, authenticate, logout

from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    ValidationError,
    SerializerMethodField,
    ChoiceField,
)

from .models import User, Employee, Customer

class EmployeeCreateSerializer(ModelSerializer):

    status = ChoiceField(choices=User.USER_TYPE)

    class Meta:
        model = Employee
        fields = [
            'username',
            'first_name',
            'last_name',
            'phone_number',
            'password',
            'email',
            'status',
        ]
        extra_kwargs = {
            'password':{'write_only': True}
        }
    
    def validate_email(self, value):
        user_qs = Employee.objects.filter(email=value)
        if user_qs.exists():
            raise ValidationError('This email is already attach to an account.')
        return value

    def create(self, validated_data):

        user_obj = Employee(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            phone_number = validated_data['phone_number'],
            status = validated_data['status']
        )
        user_obj.set_password(validated_data['password'])
        user_obj.save()

        return validated_data


class UserLoginSerializer(ModelSerializer):

    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True)
    email = EmailField(label='Email Adress', required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token',
        ]

        extra_kwargs = {'password':
                            {'write_only': True}
                        }

    def validate(self, data):
        user_obj = None
        email = data.get('email', None)
        username = data.get('username', None)
        password = data['password']

        if not email and not username:
            raise ValidationError('A username or an email is required to login')

        user = User.objects.filter(
            Q(email=email) |
            Q(username=username)
        ).distinct()

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError('This username/email is not valid')

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError('Incorrect password, pleade try again')
        else:
            raise ValidationError('Plase insert a correct login')

        data['token'] = "SOME RANDOM TOKEN"

        return data
    

class SalesContactSerializer(ModelSerializer):
    
    class Meta: 
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number']


class CustomerAccountSerializer(ModelSerializer):
        
    sales_contact = SerializerMethodField()
    
    class Meta:
        model = Customer
        fields = ['id', 'username', 'first_name', 'last_name', 
                  'email', 'status', 'phone_number', 'last_contact',
                  'company_name', 'creation_date', 'modified_date',
                  'sales_contact', 'last_contact']
        read_only_fields = ['status', 'company_name', 'sales_contact', 'last_contact']
        
    def get_sales_contact(self, instance):
        
        try:
            queryset = User.objects.get(id=instance.sales_contact.id)
            serializer = SalesContactSerializer(queryset)
            
            return serializer.data
        
        except AttributeError:
            return {}
            

class EmployeeAccountSerializer(ModelSerializer):  
    
    class Meta:
        model = Employee
        fields = ['id', 'username', 'first_name', 'last_name', 
                  'email', 'status', 'phone_number',
                  'company_name', 'creation_date', 'modified_date']

        read_only_fields = ['status', 'company_name']


class PasswordUpdateSerializer(ModelSerializer):

    new_password = CharField(max_length=128, write_only=True, required=True)
    old_password = CharField(max_length=128, write_only=True, required=True)

    class Meta:
        model = User
        fields = ['old_password', 'new_password']

    def validate_old_password(self, value):

        user = self.context['request'].user
        
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        
        user = self.context['request'].user

        instance.set_password(validated_data['new_password'])
        instance.save()

        return instance