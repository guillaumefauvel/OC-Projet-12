# Generated by Django 4.0.4 on 2022-05-17 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_prospect_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='prospect',
            name='converted',
            field=models.BooleanField(default=False),
        ),
    ]