# Generated by Django 3.2.9 on 2022-02-13 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_banner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='name_eng',
            new_name='title_eng',
        ),
        migrations.RenameField(
            model_name='banner',
            old_name='name_por',
            new_name='title_por',
        ),
        migrations.RenameField(
            model_name='banner',
            old_name='name_tet',
            new_name='title_tet',
        ),
    ]
