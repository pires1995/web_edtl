# Generated by Django 3.2.9 on 2022-02-23 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0004_ipmodel'),
        ('news', '0025_alter_newscomment_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.ManyToManyField(blank=True, null=True, related_name='post_views', to='custom.IpModel'),
        ),
    ]
