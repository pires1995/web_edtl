# Generated by Django 3.2.9 on 2022-02-12 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_alter_position_division'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='division',
            new_name='position',
        ),
    ]