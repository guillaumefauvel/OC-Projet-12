from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    USER_TYPE = [
    ('SALES','SALES'),
    ('SUPPORT','SUPPORT'),
    ('MANAGER','MANAGER'),
    ('CUSTOMER','CUSTOMER'),
    ]

    phone_number = models.CharField(max_length=20, null=True)
    creation_date = models.DateField(auto_now_add=True, null=True)
    modified_date = models.DateField(auto_now=True, null=True)

    username = models.CharField(max_length=32, unique=True, null=True)
    email = models.CharField(max_length=64, unique=True, null=True)
    first_name = models.CharField(max_length=32, null=True)
    last_name = models.CharField(max_length=32, null=True)
    password = models.CharField(max_length=128, null=True)

    status = models.CharField(max_length=10, default=USER_TYPE, null=True)

    def __str__(self):
         return self.username

    class Meta:
        ordering = ['status']
    
class Employee(User):
       
    company_name = models.CharField(max_length=100, default='EpicEvents', blank=True, null=True)
    manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = ("Employee")
        verbose_name_plural = ("Employees")
    
    
class Customer(User):
    
    company_name = models.CharField(max_length=100, blank=True, null=True)
    last_contact = models.DateField(null=True, blank=True)
    sales_contact = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = ("Customer")
        verbose_name_plural = ("Customers")
        ordering = ['last_contact']