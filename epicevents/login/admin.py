from django.contrib import admin
from .models import User, Customer, Employee

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'status')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'status', 'manager')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'company_name', 'email', 'phone_number', 'last_contact', 'sales_contact')


admin.site.register(User, UserAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Customer, CustomerAdmin)

