# Generated by Django 3.2.9 on 2022-02-01 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
