from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(User):

    USER_TYPE = [
        ('SALES','SALES'),
        ('SUPPORT','SUPPORT'),
        ('MANAGER','MANAGER'),
    ]

    status = models.CharField(max_length=10, choices=USER_TYPE)
    phone_number = models.CharField(max_length=20)
    creation_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        verbose_name = ("Employee")
        verbose_name_plural = ("Employees")


class Customer(User):

    phone_number = models.CharField(max_length=20)
    creation_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    company_name = models.CharField(max_length=100)
    sales_contact = models.ForeignKey(Employee, on_delete=models.PROTECT, blank=True, null=True)
    last_contact = models.DateField(null=True)

    def __str__(self) -> str:
        return self.company_name

    class Meta:
        verbose_name = ("Customer")
        verbose_name_plural = ("Customers")

class Prospect(models.Model):

    company_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20)
    creation_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    sales_contact = models.ForeignKey(Employee, on_delete=models.PROTECT, blank=True, null=True)
    last_contact = models.DateField(blank=True)

    def __str__(self) -> str:
        return self.company_name


class Provider(models.Model):

    PROVIDER_TYPE = [
        ('FOOD','FOOD'),
        ('GOODS','GOODS'),
        ('ANIMATION','ANIMATION'),
        ('LOGISTIC','LOGICISTIC')
    ]
    
    company_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20)
    type = models.CharField(choices=PROVIDER_TYPE, max_length=10)

    def __str__(self) -> str:
        return self.company_name


class Contract(models.Model):

    title = models.CharField(max_length=100)
    
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sales_contact = models.ForeignKey(Employee, on_delete=models.PROTECT)

    price = models.IntegerField()
    payed = models.BooleanField(default=False)
    amount_payed = models.IntegerField()

    contract_infos = models.TextField()
    signed = models.BooleanField(default=False)

    creation_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Event(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    program = models.TextField()
    
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    support_id = models.ForeignKey(Employee, on_delete=models.PROTECT)
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT)
    
    due_date = models.DateField()

    creation_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    providers = models.ManyToManyField(Provider)

    def __str__(self) -> str:
        return self.name