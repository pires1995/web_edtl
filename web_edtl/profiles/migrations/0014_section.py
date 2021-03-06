# Generated by Django 3.2.9 on 2022-02-12 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_alter_position_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_period', models.DateField(blank=True, null=True)),
                ('end_period', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True, null=True)),
                ('hashed', models.CharField(blank=True, max_length=32, null=True)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.employee')),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.division')),
            ],
        ),
    ]
