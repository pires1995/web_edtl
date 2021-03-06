# Generated by Django 3.2.9 on 2022-01-30 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('custom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_completed', models.BooleanField(default=False, null=True)),
                ('description_tet', models.TextField(blank=True, null=True)),
                ('description_por', models.TextField(blank=True, null=True)),
                ('description_eng', models.TextField(blank=True, null=True)),
                ('datetime', models.DateTimeField(null=True)),
                ('hashed', models.CharField(max_length=32, null=True)),
                ('fund', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.fund')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, null=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, null=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(blank=True, max_length=20, null=True)),
                ('longitude', models.CharField(blank=True, max_length=20, null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('hashed', models.CharField(max_length=32, null=True)),
                ('administrativepost', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='custom.administrativepost')),
                ('municipality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='custom.municipality')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projectlocation', to='project.project')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('village', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='custom.village')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectBudget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oge_estimation', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('yearly_allocation', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('owner_estimation', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('datetime', models.DateTimeField(null=True)),
                ('hashed', models.CharField(max_length=32, null=True)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projectbudget', to='project.project')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='project_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.projectcategory'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.projectstatus'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.projecttype'),
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.year'),
        ),
    ]
