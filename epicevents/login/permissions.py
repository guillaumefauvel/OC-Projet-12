import re

from django.core.exceptions import ObjectDoesNotExist
from login.exceptions import InvalidToken, MissingToken
from rest_framework import permissions
from rest_framework.authtoken.models import Token
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
    """
    List : Give the access to the Manager only, but restrict his create ability.
    Object : Give the access if the Manager is associated to the Employee.
    """
    
    def has_permission(self, request, view):
        
        if request.user.status == 'MANAGER':
            if view.action == 'create':
                return False
            return True

    def has_object_permission(self, request, view, obj):
        
        if request.user.id == obj.manager.id:
            
            return True


class CustomerListPerm(permissions.BasePermission):
    """
    List : Give the permissions if the user is a member of the staff.
    Object : If he the user is a manager, add the Update and Delete method.
    """    
    
    def has_permission(self, request, view):
        
        if request.user.status in ['MANAGER', 'SALES', 'SUPPORT']:
            return True

    def has_object_permission(self, request, view, obj):
               
        if view.action in ['update', 'partial_update', 'destroy']:
            return request.user.status == 'MANAGER'
        return True


class ProspectPerm(permissions.BasePermission):
    """
    List : Give the permission to the Managers and Sales
    Object : Give permission to access the object if the user is attached to it. Add the Delete method if he his the manager.
    """
    
    def has_permission(self, request, view):
        
        return request.user.status in ['MANAGER', 'SALES']

    def has_object_permission(self, request, view, obj):

        if request.user.id in [obj.sales_contact.manager.id, obj.sales_contact.id]:
            if view.action == 'destroy':
                return request.user.status == 'MANAGER'
            return True


class ProviderPerm(permissions.BasePermission):
    """
    List : Give access if the user is an employee. Add the Create method if he is a manager.
    Object : Give the retrieve access if the user is an employee. If the user is a Manager, give him the CRUD method.
    """
    
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
    """
    List : Give the access to create if the user is a Sales or a Manager. Return True for the other conditions.
    Object : 
     - Give the retrieve access if the user is associated to the contract. 
     - If the contract is not yet signed (by both parties) give the update access to the Customer, the Sales and the Manager
     - If the contract is signed give the update access to the Sales and the Manager
     - Give the Delete access to the Manager only
    """
    
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
        except AttributeError:
            pass
        
        if request.user.id in associated_user:

            if view.action == 'retrieve':
                return True
            elif view.action in ['update', 'partial_update']:
                if not obj.signed:
                    if request.user.status in ['CUSTOMER', 'SALES', 'MANAGER']:
                        return True 
                else:
                    if request.user.status in ['MANAGER', 'SALES']:
                        return True
            elif view.action == 'destroy':
                return request.user.status == 'MANAGER'
        

class EventPerm(permissions.BasePermission):
    """
    List : Doesn't allow the Create access.
    Object : 
    - Give access to the associated user only.
    - Give the Update access to the Manager and the Support employee.
    - Give the Delete access to the Manager only.
    """
    
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
    """
    List : Give access to the Manager only, but forbidden his Create ability.
    Object : Give access to the Manager only.
    """
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
    """
    List : Give access to every user but forbidden their Create ability
    Object : Allow every action except the Delete action.
    """

    def has_permission(self, request, view):
        
        if view.action != 'create':
            return True
        
    def has_object_permission(self, request, view, obj):
        
        if view.action == 'destroy':
            return False
        return True


