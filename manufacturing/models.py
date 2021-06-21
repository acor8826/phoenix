from django.db import models
from decimal import Decimal
from orders.models import Order, OrderItem
from formulary.models import Instruction, Instruction_Step
from inventory.models import Active
from list.models import Form, Unit, Target_Species
from inventory.models import Packaging, Excipient, Form
from formulary.models import Formula, Formula_Line
from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save, m2m_changed
from slugify import slugify
import random
from ckeditor.fields import RichTextField
# Create your models here.

class Compound_Instruction(models.Model):
	#linked_product = models.ForeignKey(Compound, on_delete=models.CASCADE,null=True, blank=True)
	instruction_form = models.ForeignKey(Form, on_delete=models.CASCADE, null=True, blank=True)
	step_no = models.IntegerField( default=0, null=True, blank=True)
	name = models.CharField(max_length=200, db_index=True, default=True, blank=True)
	class Meta:
		verbose_name = 'Instruction'
		verbose_name_plural = 'Instructions'
		ordering = ['step_no']
	def __str__(self):
		return str(self.name)

class Compounding_Instruction_Step(models.Model):
	step_no = models.IntegerField( default=0, null=True, blank=True)
	ix = RichTextField("Instruction", default=True)
	linked_instruction = models.ForeignKey(Compound_Instruction, related_name='Compound_Instruction_Step_to_Compound_Instruction', on_delete=models.CASCADE,null=True, blank=True)
	class Meta:
		verbose_name = 'Instruction Step'
		verbose_name_plural = 'Instruction Step'
		ordering = ['step_no']
	

	def __str__(self):
		return str(self.step_no)


class Compound(models.Model):
	linked_product = models.ForeignKey(Formula, on_delete=models.CASCADE,null=True, blank=True)
	name = models.CharField(max_length=200, db_index=True, null=True, blank=True)
	formula_form = models.ForeignKey(Form, on_delete=models.CASCADE, null=True, blank=True)
	qty_to_make = models.IntegerField(null=True, blank=True, default=0)
	batch_number = models.IntegerField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated = models.DateTimeField(auto_now=True, null=True, blank=True)
	#instruction = models.ManyToManyField(Compound_Instruction, related_name='Compound_to_Compound_Instruction', blank=True)

	class Meta:
		ordering = ('name',)
		index_together = (('id', 'name'),)
		verbose_name = 'Batch Record'
		verbose_name_plural = 'Batch Records'
	def save(self, *args, **kwargs):
		if self.pk is None:
			self.batch_number = random.randint(0,1000000)
			self.name=str(self.linked_product)
			self.formula_form = self.linked_product.formula_form
			super(Compound, self).save(*args, **kwargs)
	
	def __str__(self):
		return str(self.name)

	@receiver(post_save, sender=Order)
	def add_batch(sender, instance, **kwargs):
		for item in instance.items.all():
			linked_product = item.product.formula
			Compound.objects.create(linked_product=linked_product)


class Compound_Line(models.Model):
	linked_product = models.ForeignKey(Compound, related_name='compound', on_delete=models.CASCADE,null=True, blank=True)
	active = models.ForeignKey(Excipient, on_delete=models.CASCADE, null=True, blank=True)
	amount_to_weigh = models.IntegerField(default=0, null=True, blank=True)
	weighed = models.IntegerField(default=0, null=True, blank=True)
	UoM = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=200, db_index=True, default=True, blank=True)

	class Meta:
		verbose_name = 'Ingredient'
		verbose_name_plural = 'Ingredients'
		ordering = ['linked_product']

	@receiver(post_save, sender=Compound)
	def create(sender, instance, created, **kwargs):
		if created:
			for item in instance.linked_product.formula_line_set.all():
				amount = (int(item.Amount)/int(instance.linked_product.max_qty))*(int(instance.qty_to_make))
				Compound_Line.objects.create(linked_product=instance, active=item.active, amount_to_weigh=amount, UoM=item.UoM)
	

	def upper_acceptance_limit(self):
		ULT = self.amount_to_weigh*1.05
		return ULT

	def lower_acceptance_limit(self):
		LAT = self.amount_to_weigh*0.95
		return LAT
	def __str__(self):
		return str(self.active)
