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
from rest_framework.authtoken import views

import login.views as logviews
import app.views as appviews

router = routers.SimpleRouter()
router.register('employee', appviews.EmployeeViewSet, basename='employee')
router.register('customer', appviews.CustomerViewSet, basename='customer')
router.register('prospect', appviews.ProspectViewSet, basename='prospect')
router.register('free-prospect', appviews.FreeProspectViewSet, basename='free-prospect')
router.register('provider', appviews.ProviderViewSet, basename='provider')
router.register('contract', appviews.ContractViewSet, basename='contract')
router.register('event', appviews.EventViewSet, basename='event')
router.register('free-event', appviews.NotAssignedEventViewSet, basename='free-event')
router.register('account', logviews.AccountInfoView, basename='account')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include(router.urls)),

    path('home/create-employee', logviews.EmployeeCreateAPIView.as_view(), name='signup'),
    path('login/', logviews.CustomLoginView.as_view(), name='login'),
    path('login/success', logviews.SucessLogin.as_view(), name='success-login'),
    path('obtain-token/', views.obtain_auth_token),

    path('logout/', logviews.LogoutView.as_view(), name='logout'),
    path('password-update/', logviews.PasswordUpdate.as_view(), name='password-update')
]
