from django.db import models
from list.models import Form
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
# Create your models here.



class Excipient(models.Model):
	long_descr = models.CharField(max_length=256, null=True, blank=True)
	drug_form = models.ForeignKey(Form, on_delete=models.CASCADE, null=True, blank=True)
	is_active = models.BooleanField(default=False, null=True, blank=True)
	
	def __str__(self):
		return self.long_descr + " "+ str(self.drug_form)
 
class Active(models.Model):
	long_descr =  models.CharField(max_length=256, null=True, blank=True)
	drug_form = models.ForeignKey(Form, on_delete=models.CASCADE, null=True, blank=True)
	linked_excipient = models.OneToOneField(Excipient, on_delete=models.CASCADE, null=True, blank=True)
	@receiver(post_save,sender=Excipient)
	def create_active(sender, instance, **kwargs):
		if instance.is_active == True:
				Active.objects.create(long_descr = instance.long_descr,drug_form=instance.drug_form, linked_excipient=instance)
	def __str__(self):
		return str(self.long_descr) + " "+ str(self.drug_form)

class Packaging(models.Model):
	pack_desc =  models.CharField(max_length=256, null=True, blank=True)
	def __str__(self):
		return str(self.pack_desc)
	class Meta:
		ordering = ('pack_desc',)
		verbose_name = 'Packaging'
		verbose_name_plural = 'Packaging'		