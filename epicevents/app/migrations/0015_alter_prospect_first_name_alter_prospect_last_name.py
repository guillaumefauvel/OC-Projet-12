# Generated by Django 4.0.4 on 2022-05-17 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_prospect_first_name_prospect_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospect',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='prospect',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
