from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions

from login.models import User, Employee, Customer
from app.models import Prospect, Provider, Contract, Event


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


class CustomerListPerm(permissions.BasePermission):
    
    def has_permission(self, request, view):
        
        return True

    def has_object_permission(self, request, view, obj):
               
        if view.action == 'destroy':
            return request.user.status == 'MANAGER'
        return True


class ProspectPerm(permissions.BasePermission):
    
    def has_permission(self, request, view):
        
        return request.user.status in ['MANAGER', 'SALES']

    def has_object_permission(self, request, view, obj):

        if view.action == 'retrieve':
            return True
        elif view.action in ['update', 'partial_update']:        
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
            
        return True
