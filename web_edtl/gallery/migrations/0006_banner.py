# Generated by Django 3.2.9 on 2022-02-13 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import gallery.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0005_rename_galerrycategory_gallerycategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_tet', models.CharField(blank=True, max_length=200, null=True)),
                ('name_por', models.CharField(blank=True, max_length=200, null=True)),
                ('name_eng', models.CharField(max_length=200)),
                ('description_tet', models.CharField(blank=True, max_length=200, null=True)),
                ('description_por', models.CharField(blank=True, max_length=200, null=True)),
                ('description_eng', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(default='banner_default.jpg', null=True, upload_to=gallery.utils.path_and_rename_banner, verbose_name='Upload Imajen')),
                ('is_active', models.BooleanField(default=False, null=True)),
                ('datetime', models.DateTimeField(null=True)),
                ('hashed', models.CharField(blank=True, max_length=32, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]