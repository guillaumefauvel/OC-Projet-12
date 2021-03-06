from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class User(AbstractUser):

    USER_TYPE = [
    ('SALES','SALES'),
    ('SUPPORT','SUPPORT'),
    ('MANAGER','MANAGER'),
    ('CUSTOMER','CUSTOMER'),
    ]

    phone_number = models.CharField(max_length=20)
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True)
    modified_date = models.DateField(auto_now=True, null=True, blank=True)

    username = models.CharField(max_length=32, unique=True)
    email = models.CharField(max_length=64, unique=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    password = models.CharField(max_length=128)

    status = models.CharField(max_length=100, choices=USER_TYPE)

    def __str__(self):
         return self.username

    class Meta:
        ordering = ['status']
    
    
class Employee(User):
       
    company_name = models.CharField(max_length=100, default='EpicEvents')
    manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = ("Employee")
        verbose_name_plural = ("Employees")
    
    
class Customer(User):
    
    company_name = models.CharField(max_length=100, default="NoCompany")
    last_contact = models.DateField(null=True, blank=True)
    sales_contact = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = ("Customer")
        verbose_name_plural = ("Customers")
        ordering = ['last_contact']
        

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)