# Generated by Django 3.2.9 on 2022-01-31 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20220131_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='hashed',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
