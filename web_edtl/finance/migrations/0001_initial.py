# Generated by Django 3.2.9 on 2022-02-04 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import finance.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('numero_kontador', models.IntegerField()),
                ('email', models.EmailField(max_length=254, null=True)),
                ('mobile', models.IntegerField()),
                ('addresss', models.CharField(blank=True, max_length=250, null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('hashed', models.CharField(blank=True, max_length=32, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_number', models.IntegerField()),
                ('payment_date', models.DateField(null=True)),
                ('file', models.ImageField(blank=True, default='default.jpg', null=True, upload_to=finance.utils.path_and_rename_bill)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('hashed', models.CharField(blank=True, max_length=32, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.client')),
            ],
        ),
    ]
