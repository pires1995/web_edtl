# Generated by Django 3.2.9 on 2022-02-12 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0015_contactmunicipality_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmunicipality',
            name='datetitme',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='contactmunicipality',
            name='hashed',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]