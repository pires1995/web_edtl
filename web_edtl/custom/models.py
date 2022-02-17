from django.db import models

# Create your models here.
class Municipality(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		template = '{0.name}'
		return template.format(self)

class AdministrativePost(models.Model):
	municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=100)
	def __str__(self):
		template = '{0.name}'
		return template.format(self)

class Village(models.Model):
	administrativepost = models.ForeignKey(AdministrativePost, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=100)
	def __str__(self):
		template = '{0.name}'
		return template.format(self)

class Year(models.Model):
	year = models.IntegerField()
	def __str__(self):
		template = '{0.year}'
		return template.format(self)