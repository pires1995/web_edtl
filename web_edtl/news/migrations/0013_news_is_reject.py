# Generated by Django 3.2.9 on 2022-01-21 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_newsimage_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='is_reject',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
