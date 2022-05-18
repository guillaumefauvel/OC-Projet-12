from django.db import models
from django.conf import settings

from login.models import Customer, Employee

class Prospect(models.Model):

    company_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    creation_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    sales_contact = models.ForeignKey(Employee, on_delete=models.PROTECT, blank=True, null=True, related_name='prospect_sales')
    last_contact = models.DateField(blank=True, null=True)
    converted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.company_name

    class Meta:
        ordering = ['last_contact']


class Provider(models.Model):

    PROVIDER_TYPE = [
        ('FOOD','FOOD'),
        ('GOODS','GOODS'),
        ('ANIMATION','ANIMATION'),
        ('LOGISTIC','LOGISTIC')
    ]

    company_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20)
    type = models.CharField(choices=PROVIDER_TYPE, max_length=10)

    def __str__(self) -> str:
        return self.company_name


class Contract(models.Model):

    title = models.CharField(max_length=100)
    
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='contract_customer')
    sales_contact = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='contract_sales')

    price = models.IntegerField()
    payed = models.BooleanField(default=False)
    amount_payed = models.IntegerField()

    contract_infos = models.TextField()
    employee_signature = models.BooleanField(default=False)
    customer_signature = models.BooleanField(default=False)
    signed = models.BooleanField(default=False)
    history = models.TextField(blank=True, null=True)

    creation_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Event(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    program = models.TextField(blank=True, null=True)
    
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE, unique=True)
    support_id = models.ForeignKey(Employee, on_delete=models.PROTECT, blank=True, null=True, related_name='event_support')
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='event_customer')
    
    due_date = models.DateField(blank=True, null=True)

    creation_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    providers = models.ManyToManyField(Provider)

    def __str__(self) -> str:
        return self.name