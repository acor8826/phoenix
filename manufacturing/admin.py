from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Compound, Compound_Line
class CompoundItemInline(admin.TabularInline):
	model = Compound_Line
	raw_id_fields = ['linked_product']
	extra = 0

class CompoundAdmin(admin.ModelAdmin):
	fields = ('linked_product','qty_to_make','batch_number')
	list_display = ['linked_product','formula_form','qty_to_make','batch_number']
	#filter_horizontal = ('instruction',)
	inlines = [CompoundItemInline]#, Compound_InstructionItemInline]

admin.site.register(Compound, CompoundAdmin)
admin.site.register(Compound_Line)
