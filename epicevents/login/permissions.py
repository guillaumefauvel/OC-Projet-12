from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions



class IsSuperUser(permissions.BasePermission):
    """ Give the permission to CRUD any object if he is a SuperUser"""

    def has_permission(self, request, view):

        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):

        return request.user.is_superuser


    


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
        
        return request.user.status in ['MANAGER', 'SALES', 'SUPPORT']

    def has_object_permission(self, request, view, obj):
        
        if view.action == 'retrieve':
            return request.user.status in ['MANAGER', 'SALES', 'SUPPORT']
        else:
            return request.user.status == 'MANAGER'
