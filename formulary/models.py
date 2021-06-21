from django.db import models
from decimal import Decimal
from inventory.models import Active
from ckeditor.fields import RichTextField
from list.models import Form, Unit, Target_Species
from inventory.models import Packaging, Excipient, Form
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save
from django.db.models.signals import post_save
from django.utils import timezone
from slugify import slugify
from ckeditor.fields import RichTextField
from django.contrib import admin 
from nested_inline.admin import NestedModelAdmin, NestedTabularInline, NestedStackedInline

# Create your models here. Do not auto-create formula name because it might be an intermediate step
class Instruction(models.Model):
    #linked_product = models.ForeignKey(Formula, on_delete=models.CASCADE,null=True, blank=True)
    Instruction_form = models.ForeignKey(Form, on_delete=models.CASCADE, null=True, blank=True)
    step_no = models.IntegerField( default=0, null=True, blank=True)
    name = models.CharField(max_length=200, db_index=True, default=True, blank=True)
    
    class Meta:
        verbose_name = 'Instruction'
        verbose_name_plural = 'Instructions'
        ordering = ['step_no']
    def __str__(self):
        return str(self.step_no)+str("-")+str(self.name).capitalize()

class Instruction_Step(models.Model):
    step_no = models.IntegerField("sub-step",default=1, null=True, blank=True)
    ix = RichTextField("Instruction", default=True)
    linked_instruction_step = models.ForeignKey(Instruction, on_delete=models.CASCADE,null=True, blank=True)
    class Meta:
        verbose_name = 'Instruction Step'
        verbose_name_plural = 'Instruction Step'
        ordering = ['step_no']

    def __str__(self):
        return str(self.step_no)

class Formula(models.Model):
    name = models.CharField(max_length=200, db_index=True, null=True, blank=True)
    formula_form = models.ForeignKey(Form, on_delete=models.CASCADE, null=True, blank=True)
    max_qty = models.IntegerField(null=True, blank=True)
    instruction = models.ManyToManyField(Instruction, blank=True)
    in_process = models.BooleanField("Intermediate Step", default=False, null=True, blank=True)
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'name'),)
        verbose_name = 'Master Formula'
        verbose_name_plural = 'Master Formulas'
    
    def __str__(self):
        return str(self.name) + str(" ")+str(self.formula_form)+str(" ")+str(self.formula_form)+str(" ")+str(self.max_qty)

class Formula_Line(models.Model):
    linked_product = models.ForeignKey(Formula, on_delete=models.CASCADE,null=True, blank=True)
    active = models.ForeignKey(Excipient, on_delete=models.CASCADE, null=True, blank=True)
    Amount = models.IntegerField(default=0, null=True, blank=True)
    UoM = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, db_index=True, default=True, blank=True)
    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'
        ordering = ['linked_product']

