# Generated by Django 2.1.5 on 2019-02-03 21:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20190203_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]