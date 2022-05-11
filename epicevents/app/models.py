from django.db import models

from django.conf import settings


class Prospect(models.Model):

    company_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20)
    creation_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, null=True, related_name='prospect_sales')
    last_contact = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return self.company_name


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
    
    customer_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contract_customer')
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='contract_sales')

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
    support_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='event_support')
    customer_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='event_customer')
    
    due_date = models.DateField()

    creation_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    providers = models.ManyToManyField(Provider)

    def __str__(self) -> str:
        return self.name