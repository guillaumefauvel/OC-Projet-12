from django.contrib import admin

from . import models


class ProspectAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'sales_contact', 'last_contact')


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'type')
    
    
class ContractAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer_id', 'sales_contact', 'price', 'signed', 'customer_signature')


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'contract_id', 'contract_id', 'support_id', 'customer_id', 'due_date')
    

admin.site.register(models.Prospect, ProspectAdmin)
admin.site.register(models.Provider, ProviderAdmin)
admin.site.register(models.Contract, ContractAdmin)
admin.site.register(models.Event, EventAdmin)
