# Generated by Django 3.2.9 on 2022-01-26 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20220125_2220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='mission_eng',
            new_name='wwd_eng',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='mission_por',
            new_name='wwd_por',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='mission_tet',
            new_name='wwd_tet',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='vision_eng',
            new_name='wwwa_eng',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='vision_por',
            new_name='wwwa_por',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='vision_tet',
            new_name='wwwa_tet',
        ),
        migrations.AlterField(
            model_name='employee',
            name='hashed',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='end_period',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='is_active',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='start_period',
            field=models.DateField(blank=True, null=True),
        ),
    ]
