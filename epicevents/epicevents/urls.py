from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

import login.views as logviews
import app.views as appviews

router = routers.SimpleRouter()
router.register('free-employee', appviews.NotAssignedEmployeeViewSet, basename='free-employee')
router.register('employee', appviews.EmployeeViewSet, basename='employee')
router.register('customer', appviews.CustomerViewSet, basename='customer')
router.register('free-prospect', appviews.FreeProspectViewSet, basename='free-prospect')
router.register('prospect', appviews.ProspectViewSet, basename='prospect')
router.register('contract', appviews.ContractViewSet, basename='contract')
router.register('free-event', appviews.NotAssignedEventViewSet, basename='free-event')
router.register('event', appviews.EventViewSet, basename='event')
router.register('provider', appviews.ProviderViewSet, basename='provider')
router.register('account', logviews.AccountInfoView, basename='account')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include(router.urls)),

    path('home/create-employee/', logviews.EmployeeCreateAPIView.as_view(), name='signup'),
    path('login/', logviews.CustomLoginView.as_view(), name='login'),
    path('login/success', logviews.SucessLogin.as_view(), name='success-login'),
    path('login/error', logviews.LoginFailed.as_view(), name='error-login'),

    path('obtain-token/', views.obtain_auth_token),

    path('logout/', logviews.LogoutView.as_view(), name='logout'),
    path('password-update/', logviews.PasswordUpdate.as_view(), name='password-update')
]
