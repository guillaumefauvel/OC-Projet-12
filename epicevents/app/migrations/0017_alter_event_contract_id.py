# Generated by Django 4.0.4 on 2022-05-18 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_prospect_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='contract_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.contract', unique=True),
        ),
    ]
