# Generated by Django 3.2.9 on 2022-02-18 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0019_auto_20220218_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsuser',
            name='choices',
            field=models.ManyToManyField(blank=True, to='news.SubscribeChoice'),
        ),
        migrations.AlterField(
            model_name='newsuser',
            name='is_active',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
