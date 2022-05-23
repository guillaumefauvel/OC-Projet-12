import re

from django.core.exceptions import ObjectDoesNotExist
from login.exceptions import InvalidToken, MissingToken
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

from login.models import User, Employee, Customer
from app.models import Prospect, Provider, Contract, Event


class ValidToken(permissions.BasePermission):
    """ Check if the token specified is associated with the connected user """

    def has_permission(self, request, view):

        return True

        regex = re.compile('^HTTP_')
        header_infos = dict((regex.sub('', header), value) for (header, value)
                            in request.META.items() if header.startswith('HTTP_'))

        if 'AUTHORIZATION' in header_infos:
            token = header_infos['AUTHORIZATION'].split()[1]
            if Token.objects.get(user=request.user) == Token.objects.get(key=token):
                return True
            raise InvalidToken
        else: 
            raise MissingToken
        

class IsSuperUser(permissions.BasePermission):
    """ Give the permission to CRUD any object if he is a SuperUser"""

    def has_permission(self, request, view):

        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):

        return request.user.is_superuser


class IsManager(permissions.BasePermission):
    """ Give the permission to CRUD any object if he is a Manager """

    def has_permission(self, request, view):

        return request.user.status == 'MANAGER'

    def has_object_permission(self, request, view, obj):

        return request.user.status == 'MANAGER'


class EmployeePerm(permissions.BasePermission):
    
    def has_permission(self, request, view):
        
        if request.user.status == 'MANAGER':
            return True

    def has_object_permission(self, request, view, obj):
        
        if request.user.id == obj.manager.id:
            
            return True


class CustomerListPerm(permissions.BasePermission):
    
    def has_permission(self, request, view):
        
        if request.user.status in ['MANAGER', 'SALES', 'SUPPORT']:
            return True

    def has_object_permission(self, request, view, obj):
               
        if view.action in ['update', 'partial_update', 'destroy']:
            return request.user.status == 'MANAGER'
        return True


class ProspectPerm(permissions.BasePermission):
    
    def has_permission(self, request, view):
        
        return request.user.status in ['MANAGER', 'SALES']

    def has_object_permission(self, request, view, obj):

        if request.user.id in [obj.sales_contact.manager.id, obj.sales_contact.id]:
            if view.action in ['retrieve', 'update', 'partial_update']:
                return True
            elif view.action == 'destroy':
                return request.user.status == 'MANAGER'


class ProviderPerm(permissions.BasePermission):
    
    def has_permission(self, request, view):
        
        if view.action == 'create':
            return request.user.status == 'MANAGER'
        
        return request.user.status in ['MANAGER', 'SALES', 'SUPPORT']

    def has_object_permission(self, request, view, obj):
               
        if view.action == 'retrieve':
            return request.user.status in ['MANAGER', 'SALES', 'SUPPORT']
        else:
            return request.user.status == 'MANAGER'


class ContractPerm(permissions.BasePermission):
    
    def has_permission(self, request, view):

        if view.action == 'create':
            if request.user.status in ['CUSTOMER', 'SUPPORT']:
                return False
        return True

    def has_object_permission(self, request, view, obj):
        
        associated_user = [
            obj.customer_id.id,
            obj.sales_contact.id,
            obj.sales_contact.manager.id,
        ]

        try:
            associated_user.append(Event.objects.get(contract_id=obj.id).support_id.id)
        except ObjectDoesNotExist:
            pass
        
        if request.user.id in associated_user:

            if view.action == 'retrieve':
                return True
            elif view.action in ['update', 'partial_update']:
                if not obj.signed:
                    if request.user.status in ['CUSTOMER', 'SALES', 'MANAGER']:
                        return True 
                else:
                    if request.user.status == 'MANAGER':
                        return True
            elif view.action == 'destroy':
                return request.user.status == 'MANAGER'
        

class EventPerm(permissions.BasePermission):
    
    def has_permission(self, request, view):
        
        if view.action == 'create':
            return False
        return True

    def has_object_permission(self, request, view, obj):
        
        associated_user = [
            obj.customer_id.id,
            obj.support_id.id,
            obj.support_id.manager.id,
            Contract.objects.get(id=obj.contract_id.id).sales_contact.id,
        ]
                
        if request.user.id in associated_user:
            if view.action == 'retrieve':
                return True
            
            if view.action in ['update', 'partial_update']:
                return request.user.status in ['MANAGER', 'SUPPORT']
        
            if view.action == 'destroy':
                return request.user.status == 'MANAGER'


class FreeEventPerm(permissions.BasePermission):
    
    def has_permission(self, request, view):
        
        if request.user.status == 'MANAGER':
            if view.action == 'create':
                return False
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        
        if request.user.status == 'MANAGER':
            return True
        

class AccountPerm(permissions.BasePermission):
    
    
    def has_permission(self, request, view):
        
        if view.action != 'create':
            return True
        
    def has_object_permission(self, request, view, obj):
        
        if view.action == 'destroy':
            return False
        return True


