# Generated by Django 4.0.4 on 2022-05-09 12:20

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('payed', models.BooleanField(default=False)),
                ('amount_payed', models.IntegerField()),
                ('contract_infos', models.TextField()),
                ('signed', models.BooleanField(default=False)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('modified_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=20)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('modified_date', models.DateField(auto_now=True)),
                ('company_name', models.CharField(max_length=100)),
                ('last_contact', models.DateField(null=True)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('status', models.CharField(choices=[('SALES', 'SALES'), ('SUPPORT', 'SUPPORT'), ('MANAGER', 'MANAGER')], max_length=10)),
                ('phone_number', models.CharField(max_length=20)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('modified_date', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('program', models.TextField()),
                ('due_date', models.DateField()),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('modified_date', models.DateField(auto_now=True)),
                ('contract_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.contract')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Prospect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('modified_date', models.DateField(auto_now=True)),
                ('last_contact', models.DateField(blank=True)),
                ('sales_contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('FOOD', 'FOOD'), ('GOODS', 'GOODS'), ('ANIMATION', 'ANIMATION'), ('LOGISTIC', 'LOGICISTIC')], max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='event',
            name='providers',
            field=models.ManyToManyField(to='app.provider'),
        ),
        migrations.AddField(
            model_name='event',
            name='support_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.employee'),
        ),
        migrations.AddField(
            model_name='customer',
            name='sales_contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.employee'),
        ),
        migrations.AddField(
            model_name='contract',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer'),
        ),
        migrations.AddField(
            model_name='contract',
            name='sales_contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.employee'),
        ),
    ]
