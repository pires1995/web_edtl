# Generated by Django 3.2.9 on 2022-02-12 01:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointment', '0013_rename_is_finish_appointment_is_cancelled'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254, null=True)),
                ('email', models.CharField(max_length=254, null=True)),
                ('mobile', models.IntegerField(null=True)),
                ('text', models.TextField(null=True)),
                ('submit_date', models.DateTimeField(null=True)),
                ('hashed', models.CharField(blank=True, max_length=32, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactMunicipality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('phone_number', models.IntegerField()),
                ('municipality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.municipality')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.position')),
            ],
        ),
    ]
