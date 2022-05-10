from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet

from .serializers import UserCreateSerializer, AccountSerializer
from login.models import User
from . import exceptions

class UserCreateAPIView(CreateAPIView):
    """ Allow the registration of a new user """

    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class LogoutView(APIView):
    """ Disconnect the user from his account """
    def get(self, request):
        logout(request)

        return Response({'Disconnected': 'You\'ve successfully logged out'})


@permission_classes([IsAuthenticated])
class SucessLogin(APIView):
    """ Informs the user that he successfully logged in """
    def get(self, request):
        return Response({'Success': 'You\'ve successfully logged in'})


class CustomLoginView(LoginView):
    """ Log a new user by checking his credentials """

    template_name = 'admin/login.html'

    def post(self, request, *args, **kwargs):

        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username=username).first()
        
        if user is None:
            raise exceptions.UserNotFound
        if not user.check_password(password):
            print(password)
            raise exceptions.BadPassword
            
        user = authenticate(username=username, password=password)
        login(request, user)

        response = HttpResponseRedirect('/login/success')

        return response
    

class MultipleSerializerMixin:
    """
    Mixin that allow the use of a detailled serializer class
    """

    detail_serializer_class = None

    def get_serializer_class(self):

        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


@permission_classes([IsAuthenticated])
class AccountInfoView(MultipleSerializerMixin, ModelViewSet):
    
    serializer_class = AccountSerializer
    detail_serializer_class = AccountSerializer

    def get_queryset(self):

        return [User.objects.get(id=self.request.user.id)]
            