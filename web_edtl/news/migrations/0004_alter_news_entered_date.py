# Generated by Django 3.2.9 on 2022-01-19 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20220119_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='entered_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
