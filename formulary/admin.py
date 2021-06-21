from django.contrib import admin
from .models import Formula, Formula_Line, Instruction, Instruction_Step
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.contrib import admin 
from nested_inline.admin import NestedModelAdmin, NestedTabularInline, NestedStackedInline

#class Instruction_StepItemInline(NestedStackedInline):
#	model = Instruction_Step
#	extra = 0

#class InstructionInline(NestedTabularInline):
#	list_display = ['']
#	model = Instruction
#	inlines = [Instruction_StepItemInline]
#	extra = 0

class FormulaItemInline(admin.TabularInline):
	model = Formula_Line
	raw_id_fields = ['linked_product']
	extra = 0

class FormulaAdmin(admin.ModelAdmin):
    list_display = ['name','formula_form',]#,'slug','available', 'created', 'updated']
    #list_filter = ['available', 'created', 'updated']
    #list_editable = ['available']
    #prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('instruction',)
    inlines = [FormulaItemInline]

class Instruction_StepInline(admin.TabularInline):
    #fields = ('product','packaging','pet','doctor','price','quantity','tax','tot_cost')
    model = Instruction_Step
    raw_id_fields = ['linked_instruction_step']
    extra = 0

class InstructionAdmin(admin.ModelAdmin):
	list_display = ['step_no','name','Instruction_form']
	list_editable = ['step_no',]
	list_filter = ['Instruction_form',]
	list_display_links = ['name']
	inlines = [Instruction_StepInline]

admin.site.register(Formula, FormulaAdmin)
admin.site.register(Instruction, InstructionAdmin)

