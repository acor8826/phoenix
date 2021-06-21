from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from Product.models import Product
import uuid
import datetime
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import random
# Create your models here.
class Pharmacy(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, blank=True, null=True)
	pharmacy_name = models.CharField(max_length=200, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	address = models.CharField(max_length=250, blank=True, null=True)
	postal_code = models.CharField(max_length=20, blank=True, null=True)
	city = models.CharField(max_length=100, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	updated = models.DateTimeField(auto_now=True, blank=True, null=True)
	product = models.ManyToManyField(Product, blank=True)
	class Meta:
		ordering = ('pharmacy_name',)


	def __str__(self):
		return str(self.pharmacy_name)

class Pharmacist(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, blank=True, null=True)
	first_name = models.CharField(max_length=50, blank=True, null=True)
	last_name = models.CharField(max_length=50, blank=True, null=True)
	email = models.EmailField()
	rego_number = models.CharField(max_length=50, blank=True, null=True)
	mobile_number = models.CharField(max_length=50, blank=True, null=True)
	pharmacy_name = models.ForeignKey(Pharmacy, on_delete=models.CASCADE, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	class Meta:
		ordering = ('last_name',)
		verbose_name = ('Pharmacist')
		verbose_name_plural = ('Pharmacists')
	


	def __str__(self):
		return str(self.last_name) + " " + str(self.first_name)


class Technician(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, blank=True, null=True)
	first_name = models.CharField(max_length=50, blank=True, null=True)
	last_name = models.CharField(max_length=50, blank=True, null=True)
	mobile_number = models.CharField(max_length=50, blank=True, null=True)
	pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	class Meta:
		ordering = ('last_name',)
		verbose_name = ('Technician')
		verbose_name_plural = ('Techician')

class ClinicGroup(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
	group_name = models.CharField(max_length=200, blank=True, null=True)
	contact_email = models.EmailField(blank=True, null=True)
	address = models.CharField(max_length=250, blank=True, null=True)
	postal_code = models.CharField(max_length=20, blank=True, null=True)
	city = models.CharField(max_length=100, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	class Meta:
		ordering = ('group_name',)
		verbose_name = ('Group')
		verbose_name_plural = ('Group')

	
	def __str__(self):
		return str(self.group_name )

class Clinic(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, unique=True)
	clinic_name = models.CharField(max_length=200, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	address = models.CharField(max_length=250, blank=True, null=True)
	postal_code = models.CharField(max_length=20)
	city = models.CharField(max_length=100, blank=True, null=True)
	clinic = models.ForeignKey(ClinicGroup, on_delete=models.CASCADE, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	class Meta:
		ordering = ('clinic_name',)
		verbose_name = ('Clinic')
		verbose_name_plural = ('Clinics')

	
	def __str__(self):
		return str(self.clinic_name )

class Practitioner(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, blank=True, null=True)
	first_name = models.CharField(max_length=50, blank=True, null=True)
	last_name = models.CharField(max_length=50, blank=True, null=True)
	email = models.EmailField()
	prescriber_number = models.CharField(max_length=50, blank=True, null=True)
	mobile_number = models.CharField(max_length=50, blank=True, null=True)
	clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	class Meta:
		ordering = ('last_name',)
		verbose_name = ('Vet')
		verbose_name_plural = ('Vets')
	
	def __str__(self):
		return str(self.last_name) + " " + str(self.first_name)

class Nurse(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
	first_name = models.CharField(max_length=50, blank=True, null=True)
	last_name = models.CharField(max_length=50, blank=True, null=True)
	email = models.EmailField()
	mobile_number = models.CharField(max_length=50, blank=True, null=True)
	clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
	class Meta:
		ordering = ('last_name',)
		verbose_name = ('Vet Nurse')
		verbose_name_plural = ('Vet Nurses')
	


	def __str__(self):
		return str(self.last_name) + " " + str(self.first_name)


class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
	clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, blank=True, null=True)
	#first_name = models.CharField(max_length=50, blank=True, null=True)
	#last_name = models.CharField(max_length=50, blank=True, null=True)
	address = models.CharField(max_length=250, blank=True, null=True)
	postal_code = models.CharField(max_length=20, blank=True, null=True)
	city = models.CharField(max_length=100, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	class Meta:
		ordering = ('user',)

	def __str__(self):
		return str(self.user)

class Pet(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	owner = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)

	class Meta:
		ordering = ('owner',)
		verbose_name = 'Pet'
		verbose_name_plural = 'Pets'
	def __str__(self):
		return str(self.name)
