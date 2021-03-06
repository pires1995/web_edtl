# Generated by Django 3.2.9 on 2022-02-15 10:06

from django.db import migrations, models
import profiles.utils


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0021_auto_20220215_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_tet', models.CharField(blank=True, max_length=250, null=True)),
                ('title_por', models.CharField(blank=True, max_length=250, null=True)),
                ('title_eng', models.CharField(blank=True, max_length=250, null=True)),
                ('description_tet', models.TextField(blank=True, null=True)),
                ('description_por', models.TextField(blank=True, null=True)),
                ('description_eng', models.TextField(blank=True, null=True)),
                ('icon', models.CharField(blank=True, max_length=300, null=True)),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to=profiles.utils.path_and_rename_service)),
                ('hashed', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
    ]
