# Generated by Django 4.0.4 on 2022-05-17 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_alter_customer_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['last_contact'], 'verbose_name': 'Customer', 'verbose_name_plural': 'Customers'},
        ),
    ]
