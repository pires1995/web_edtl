# Generated by Django 3.2.9 on 2022-02-20 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0023_auto_20220220_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='newscomment',
            name='is_admin',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
