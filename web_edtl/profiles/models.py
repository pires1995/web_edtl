from django.db import models
from .utils import path_and_rename_orgchart, path_and_rename_about
import hashlib


# Create your models here.
class About(models.Model):
    intro_tet=models.TextField(null=True, blank=True)
    intro_por=models.TextField(null=True, blank=True)
    intro_eng=models.TextField(null=True, blank=True)
    wwa_tet = models.TextField(null=True, blank=True)
    wwa_por = models.TextField(null=True, blank=True)
    wwa_eng = models.TextField(null=True, blank=True)
    wwd_tet = models.TextField(null=True, blank=True)
    wwd_por = models.TextField(null=True, blank=True)
    wwd_eng = models.TextField(null=True, blank=True)
    motto_tet = models.TextField(null=True, blank=True)
    motto_por = models.TextField(null=True, blank=True)
    motto_eng = models.TextField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to=path_and_rename_about, null=True, blank=True)
    org_chart = models.FileField(upload_to=path_and_rename_orgchart, null=True, blank=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        template = '{0.wwa_tet}'
        return template.format(self)

    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(About, self).save(*args, **kwargs)


# TEAM
class Division(models.Model):
    code = models.CharField(max_length=20, null=True)
    name_tet = models.CharField(max_length=50, null=True, blank=True)
    name_por = models.CharField(max_length=50, null=True, blank=True)
    name_eng = models.CharField(max_length=50, null=True, blank=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        template = '{0.code} , {0.name_tet}'
        return template.format(self)
    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(Division, self).save(*args, **kwargs)


class Employee(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    sex = models.CharField(choices=[('Male','Male'),('Female','Female')], max_length=6, null=True, blank=True)
    image = models.ImageField(default='person.jpg', upload_to='employee_image/', null=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)
    mobile = models.IntegerField(null=True)
    email = models.EmailField(max_length=254, null=True)
    def __str__(self):
        template = '{0.first_name} {0.last_name}'
        return template.format(self)
    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(Employee, self).save(*args, **kwargs)


class Position(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, null=True, related_name='position')
    start_period = models.DateField(null=True, blank=True)
    end_period = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        template = '{0.division} | {0.employee}'
        return template.format(self)
    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(Position, self).save(*args, **kwargs)
