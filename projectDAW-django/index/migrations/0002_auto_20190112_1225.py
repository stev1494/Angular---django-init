# Generated by Django 2.1.4 on 2019-01-12 17:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('service', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('price', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('price', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service_Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_appointment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.Appointment')),
                ('id_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.Service')),
            ],
        ),
        migrations.CreateModel(
            name='Service_Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.Service')),
            ],
        ),
        migrations.CreateModel(
            name='Service_Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Work_Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=100)),
                ('salary', models.FloatField(default=500)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AddField(
            model_name='service_employee',
            name='id_employee_area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.Work_Area'),
        ),
        migrations.AddField(
            model_name='service_employee',
            name='id_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.Service'),
        ),
        migrations.AddField(
            model_name='service_area',
            name='id_work_area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.Work_Area'),
        ),
        migrations.AddField(
            model_name='market',
            name='id_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.Product'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='id_client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.Client'),
        ),
        migrations.AddField(
            model_name='admin',
            name='id_employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.Employee'),
        ),
        migrations.AddField(
            model_name='user',
            name='id_client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.Client'),
        ),
    ]
