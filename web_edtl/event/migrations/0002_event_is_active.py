# Generated by Django 3.2.9 on 2022-01-28 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_active',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
