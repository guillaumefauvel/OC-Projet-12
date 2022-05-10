from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, mixins

from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin
)

from login.models import User
from .models import Prospect, Provider, Contract, Event
from .serializers import (CustomerSerializer,
                          EmployeeSerializer,
                          ProspectSerializer,
                          ProviderSerializer,
                          ContractSerializer,
                          EventSerializer,
                          )


class ManagerEmployeeViewSet(RetrieveModelMixin, ListModelMixin, viewsets.GenericViewSet):
    
    
    serializer_class = EmployeeSerializer

    def get_queryset(self):

        print(self.request.user)

        return User.objects.all()


class ManagerCustomerViewSet(RetrieveModelMixin, ListModelMixin, viewsets.GenericViewSet):
    
    serializer_class = CustomerSerializer

    def get_queryset(self):

        return User.objects.all()
    

class ManagerProspectViewSet(ModelViewSet):
    
    serializer_class = ProspectSerializer

    def get_queryset(self):

        return Prospect.objects.all()
    
    
class ManagerProviderViewSet(ModelViewSet):
    
    serializer_class = ProviderSerializer

    def get_queryset(self):

        return Provider.objects.all()
    
    
class ManagerContractViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, viewsets.GenericViewSet):
    
    serializer_class = ContractSerializer

    def get_queryset(self):

        return Contract.objects.all()


class ManagerEventViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, viewsets.GenericViewSet):
    
    serializer_class = EventSerializer

    def get_queryset(self):

        return Event.objects.all()