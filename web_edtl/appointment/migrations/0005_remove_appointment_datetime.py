# Generated by Django 3.2.9 on 2022-02-04 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_auto_20220204_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='datetime',
        ),
    ]
