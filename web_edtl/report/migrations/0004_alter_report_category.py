# Generated by Django 3.2.9 on 2022-01-29 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0004_auto_20220128_1524'),
        ('report', '0003_report_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.department'),
        ),
    ]
