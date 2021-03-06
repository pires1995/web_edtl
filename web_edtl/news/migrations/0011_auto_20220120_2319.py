# Generated by Django 3.2.9 on 2022-01-20 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='language',
            field=models.CharField(choices=[('Tetum', 'Tetum'), ('Portugues', 'Portugues'), ('English', 'English')], max_length=10, null=True, verbose_name='News Languages'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.newscategory', verbose_name='News Category'),
        ),
        migrations.AlterField(
            model_name='newsimage',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
