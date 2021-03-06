# Generated by Django 3.2.9 on 2022-01-20 02:31

from django.db import migrations
import imagekit.models.fields
import news.utils


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to=news.utils.path_and_rename_news, verbose_name='Upload Imajen'),
        ),
    ]
