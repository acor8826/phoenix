from django.db import models

# Create your models here.
class Unit(models.Model):
	short_list = models.CharField(max_length=10)
	long_descr =  models.CharField(max_length=10)

	def __str__(self):
		return self.short_list

class Form(models.Model):
	desc = models.CharField(max_length=255)

	def __str__(self):
		return self.desc
		
class Target_Species(models.Model):
	name = models.CharField(max_length=255)
	class Meta:
		ordering = ('name',)
		verbose_name = 'Target species'
		verbose_name_plural = 'Target species'

	def __str__(self):
		return self.name
