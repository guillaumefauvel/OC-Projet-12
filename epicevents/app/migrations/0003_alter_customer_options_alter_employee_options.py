# Generated by Django 4.0.4 on 2022-05-09 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_contract_customer_employee_event_prospect_provider_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Customer', 'verbose_name_plural': 'Customers'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Employee', 'verbose_name_plural': 'Employees'},
        ),
    ]
