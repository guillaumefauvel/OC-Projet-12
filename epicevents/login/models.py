

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class User(User):

#     USER_TYPE = [
#         ('SALES','SALES'),
#         ('SUPPORT','SUPPORT'),
#         ('MANAGER','MANAGER'),
#         ('CUSTOMER','CUSTOMER'),
#     ]

#     status = models.CharField(max_length=10, choices=USER_TYPE)
#     phone_number = models.CharField(max_length=20)
#     creation_date = models.DateField(auto_now_add=True)
#     modified_date = models.DateField(auto_now=True)

#     # CUSTOMER ATTRIBUTES
#     company_name = models.CharField(max_length=100, blank=True, null=True)
#     last_contact = models.DateField(null=True, blank=True)

#     def __str__(self) -> str:
#         return super().__str__()


class User(AbstractUser):
    USER_TYPE = [
        ('SALES','SALES'),
        ('SUPPORT','SUPPORT'),
        ('MANAGER','MANAGER'),
        ('CUSTOMER','CUSTOMER'),
    ]
    
    status = models.CharField(max_length=10, choices=USER_TYPE, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    creation_date = models.DateField(auto_now_add=True, null=True)
    modified_date = models.DateField(auto_now=True, null=True)
    
    username = models.CharField(max_length=32, unique=True, null=True)
    email = models.CharField(max_length=64, unique=True, null=True)
    first_name = models.CharField(max_length=32, null=True)
    last_name = models.CharField(max_length=32, null=True)
    password = models.CharField(max_length=128, null=True)
    
    # CUSTOMER ATTRIBUTES
    
    company_name = models.CharField(max_length=100, blank=True, null=True)
    last_contact = models.DateField(null=True, blank=True)
    
    def __str__(self) -> str:
         return super().__str__()