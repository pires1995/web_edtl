# Generated by Django 3.2.9 on 2022-02-23 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0003_auto_20220216_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='is_send_notif',
            field=models.BooleanField(default=False, null=True),
        ),
    ]