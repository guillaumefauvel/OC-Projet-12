# Generated by Django 4.0.4 on 2022-05-17 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_alter_customer_sales_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['-sales_contact'], 'verbose_name': 'Customer', 'verbose_name_plural': 'Customers'},
        ),
    ]
