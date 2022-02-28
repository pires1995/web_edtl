from django.db import models
from .utils import path_and_rename_orgchart, path_and_rename_about, path_and_rename_service,path_and_rename_deliverasaun
import hashlib
from main.models import User
from django.core.validators import FileExtensionValidator

GroupChoice = [
    ('Board Member', 'Board Member'),
    ('Department', 'Department'),
    ('Division', 'Division'),
    ('Gabineti Apoiu Servisu', 'Gabineti Apoiu Servisu'),
    ('Project Management Unit', 'Project Management Unit'),
    ('Auditoria', 'Auditoria'),
    ('Executive Directors', 'Executive Directors'),
]
# Create your models here.
class About(models.Model):
    background_tet=models.TextField(null=True, blank=True)
    background_por=models.TextField(null=True, blank=True)
    background_eng=models.TextField(null=True, blank=True)
    mission_tet = models.TextField(null=True, blank=True)
    mission_por = models.TextField(null=True, blank=True)
    mission_eng = models.TextField(null=True, blank=True)
    vision_tet = models.TextField(null=True, blank=True)
    vision_por = models.TextField(null=True, blank=True)
    vision_eng = models.TextField(null=True, blank=True)
    values_tet = models.TextField(null=True, blank=True)
    values_por = models.TextField(null=True, blank=True)
    values_eng = models.TextField(null=True, blank=True)
    objective_tet = models.TextField(null=True, blank=True)
    objective_por = models.TextField(null=True, blank=True)
    objective_eng = models.TextField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to=path_and_rename_about, null=True, blank=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        template = '{0.background_tet}'
        return template.format(self)

    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(About, self).save(*args, **kwargs)

class Service(models.Model):
    title_tet=models.CharField(max_length=250,null=True, blank=True)
    title_por=models.CharField(max_length=250,null=True, blank=True)
    title_eng=models.CharField(max_length=250,null=True, blank=True)
    description_tet = models.CharField(max_length=200,null=True, blank=True)
    description_por = models.CharField(max_length=200,null=True, blank=True)
    description_eng = models.CharField(max_length=200,null=True, blank=True)
    icon = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to=path_and_rename_service, null=True, blank=True)
    is_active = models.BooleanField(default=False, null=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        template = '{0.title_tet} - {0.title_eng}'
        return template.format(self)

    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(Service, self).save(*args, **kwargs)



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
    resume = models.TextField(null=True)
    def __str__(self):
        template = '{0.first_name} {0.last_name}'
        return template.format(self)
    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(Employee, self).save(*args, **kwargs)


class Position(models.Model):
    position = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, related_name='position')
    is_active = models.BooleanField(default=False, null=True)
    group = models.CharField(choices=GroupChoice, null=True, max_length=200)
    hashed = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        template = '{0.position} | {0.employee}'
        return template.format(self)
    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(Position, self).save(*args, **kwargs)

class Department(models.Model):
    position = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    start_period = models.DateField(null=True, blank=True)
    end_period = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=False, null=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        template = '{0.division} | {0.employee}'
        return template.format(self)
    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(Department, self).save(*args, **kwargs)

class Section(models.Model):
    position = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    start_period = models.DateField(null=True, blank=True)
    end_period = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=False, null=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        template = '{0.division} | {0.employee}'
        return template.format(self)
    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(Section, self).save(*args, **kwargs)

class Deliverasaun(models.Model):
    title_tet = models.CharField(max_length=254, null=False)
    title_por = models.CharField(max_length=254, null=True)
    title_eng = models.CharField(max_length=254, null=True)
    description_tet = models.TextField(null=True, blank=True)
    description_por = models.TextField(null=True, blank=True)
    description_eng = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to=path_and_rename_deliverasaun,
                            validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    is_active = models.BooleanField(default=False, null=True)
    date = models.DateField(null=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)
    def __str__(self):
        template = '{0.name_tet}'
        return template.format(self)

    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(Deliverasaun, self).save(*args, **kwargs)