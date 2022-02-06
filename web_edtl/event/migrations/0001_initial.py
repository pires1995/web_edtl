# Generated by Django 3.2.9 on 2022-01-28 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import event.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_tet', models.CharField(max_length=254)),
                ('name_por', models.CharField(max_length=254, null=True)),
                ('name_eng', models.CharField(max_length=254, null=True)),
                ('overview_tet', models.TextField(blank=True, null=True)),
                ('overview_por', models.TextField(blank=True, null=True)),
                ('overview_eng', models.TextField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to=event.utils.path_and_rename_event)),
                ('datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('hashed', models.CharField(blank=True, max_length=32, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
