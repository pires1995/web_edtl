from django.db import models
import hashlib
from custom.models import Municipality, AdministrativePost, Village
from main.models import User
from django.core.validators import FileExtensionValidator


class Year(models.Model):
	year = models.IntegerField(null=True)
	def __str__(self):
		template = '{0.year}'
		return template.format(self)

class ProjectStatus(models.Model):
	status = models.CharField(max_length=100)
	def __str__(self):
		return self.status

class Fund(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class TypeOfProcurament(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class ProjectCategory(models.Model):
	code = models.CharField(max_length=10, null=True)
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name



class Project(models.Model):
    name = models.CharField(max_length=500, null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, null=True)
    project_status = models.ForeignKey(ProjectStatus, on_delete=models.CASCADE, null=True)
    project_category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, null=True)
    fund = models.ForeignKey(Fund, on_delete=models.CASCADE, null=True)
    typeofprocurament = models.ForeignKey(TypeOfProcurament, on_delete=models.CASCADE, null=True, verbose_name="Type of Procurament")
    is_active = models.BooleanField(default=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    contract_number = models.CharField(max_length=300, null=True, blank=True)
    is_completed = models.BooleanField(default=False, null=True)
    description_tet = models.TextField(null=True, blank=True)
    description_por = models.TextField(null=True, blank=True)
    description_eng = models.TextField(null=True, blank=True)
    start_period = models.DateField(null=True, blank=True)
    end_period = models.DateField(null=True, blank=True)
    datetime = models.DateTimeField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)
    
    def __str__(self):
        template = '{0.name}'
        return template.format(self)
    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(Project, self).save(*args, **kwargs)
    
class ProjectLocation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, related_name="projectlocation")
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, null=True, blank=False)
    administrativepost = models.ForeignKey(AdministrativePost, on_delete=models.CASCADE, null=True, blank=True)
    village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True, blank=True)
    latitude = models.CharField(max_length=20, null=True, blank=True)
    longitude = models.CharField(max_length=20, null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)
    def __str__(self):
        template = '{0.project.name}'
        return template.format(self)
    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(ProjectLocation, self).save(*args, **kwargs)


class ProjectBudget(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, related_name="projectbudget")
    budget = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        template = '{0.project.name}'
        return template.format(self)
    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(ProjectBudget, self).save(*args, **kwargs)
