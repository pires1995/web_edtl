# Generated by Django 3.2.9 on 2022-02-09 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_alter_employee_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='division',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.division'),
        ),
    ]