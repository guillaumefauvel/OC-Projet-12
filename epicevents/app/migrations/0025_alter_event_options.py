# Generated by Django 4.0.4 on 2022-05-25 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_contract_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-modified_date']},
        ),
    ]
