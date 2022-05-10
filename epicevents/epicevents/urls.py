"""epicevents URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from app.views import (
    ManagerEmployeeViewSet,
    ManagerCustomerViewSet,
    ManagerProspectViewSet,
    ManagerProviderViewSet,
    ManagerContractViewSet,
    ManagerEventViewSet,
)

from login.views import (
    UserCreateAPIView,
    CustomLoginView,
    SucessLogin,
    LogoutView,
)

router = routers.SimpleRouter()

router.register('employee', ManagerEmployeeViewSet, basename='employee')
router.register('customer', ManagerCustomerViewSet, basename='customer')
router.register('prospect', ManagerProspectViewSet, basename='prospect')
router.register('provider', ManagerProviderViewSet, basename='provider')
router.register('contract', ManagerContractViewSet, basename='contract')
router.register('event', ManagerEventViewSet, basename='event')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
    path('signup/', UserCreateAPIView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('login/success', SucessLogin.as_view(), name='success-login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
