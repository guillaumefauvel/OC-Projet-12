from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from . import serializers as logserializer
from login.models import User, Customer, Employee
from . import exceptions, permissions


@permission_classes([permissions.IsManager, permissions.ValidToken])
class EmployeeCreateAPIView(CreateAPIView):
    """ Allow the registration of a new user """

    serializer_class = logserializer.EmployeeCreateSerializer
    queryset = Employee.objects.all()


@permission_classes([IsAuthenticated])
class LogoutView(APIView):
    """ Disconnect the user from his account """
    
    def get(self, request):
        logout(request)

        return Response({'Disconnected': 'You\'ve successfully logged out'})


@permission_classes([IsAuthenticated, permissions.ValidToken])
class PasswordUpdate(UpdateAPIView):
    """     Update the password of the authenticated user     """
    serializer_class = logserializer.PasswordUpdateSerializer

    def get_queryset(self):
        user_obj = User.objects.get(id=self.request.user.id)

        return user_obj

    def get_object(self):
       
        user_obj = User.objects.get(id=self.request.user.id)

        return user_obj


@permission_classes([IsAuthenticated])
class SucessLogin(APIView):
    """ Informs the user that he successfully logged in """
    def get(self, request):
        return Response({'Success': 'You\'ve successfully logged in'})


class LoginFailed(APIView):
    """ Informs the user that his login attempt failed """
    def get(self, request):
        return Response({'Error': 'You\'re login credentials are invalid'})


class CustomLoginView(LoginView):
    """ Log a new user by checking his credentials """

    template_name = 'admin/login.html'

    def post(self, request, *args, **kwargs):

        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            return HttpResponseRedirect('/login/error')
        if not user.check_password(password):
            return HttpResponseRedirect('/login/error')
            
        user = authenticate(username=username, password=password)
        login(request, user)

        response = HttpResponseRedirect('/login/success')

        return response
    

class MultipleSerializerMixin:
    """ Mixin that allow the use of a detailled serializer class """

    employee_serializer_class = None

    def get_serializer_class(self):

        if User.objects.get(id=self.request.user.id).status != 'CUSTOMER' and self.employee_serializer_class is not None:
            return self.employee_serializer_class

        return super().get_serializer_class()


@permission_classes([IsAuthenticated, permissions.AccountPerm, permissions.ValidToken])
class AccountInfoView(MultipleSerializerMixin, ModelViewSet):
    """ Return the infos of the authenticated user. """
    
    serializer_class = logserializer.CustomerAccountSerializer
    employee_serializer_class = logserializer.EmployeeAccountSerializer

    def get_queryset(self):
        user_obj = User.objects.get(id=self.request.user.id)
        if user_obj.status == 'CUSTOMER':
            return Customer.objects.filter(id=self.request.user.id)
        return User.objects.filter(id=self.request.user.id)
            