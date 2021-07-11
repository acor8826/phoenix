from django.contrib import admin
from . models import ClinicGroup, Clinic, Practitioner, Nurse, Customer, Pet, Pharmacy, Pharmacist, Technician  
# Register your models here.
###CUSTOMER####
class PetItemInline(admin.TabularInline):
	model = Pet
	raw_id_fields = ['owner']
	extra = 0
class CustomerAdmin(admin.ModelAdmin):
	fields = ('user','address', 'city','postal_code')
	list_display = ['user','address', 'city','postal_code','created']
	inlines = [PetItemInline]
###GROUP####
class ClinicItemInline(admin.TabularInline):
	model = Clinic
	raw_id_fields = ['clinic']
	extra=0
class GroupAdmin(admin.ModelAdmin):
	fields = ('group_name','contact_email', 'address', 'city','postal_code', 'user')
	list_display = ['group_name','contact_email', 'address', 'city','postal_code']
	inlines = [ClinicItemInline]
class PractitionerItemInline(admin.TabularInline):
	model = Practitioner
	raw_id_fields = ['clinic']
	extra=0
####CLINIC#####
class PractitionerItemInline(admin.TabularInline):
	model = Practitioner
	raw_id_fields = ['clinic']
	extra=0
class NurseItemInline(admin.TabularInline):
	model = Nurse
	raw_id_fields = ['clinic']
	extra=0
class CustomerItemInline(admin.TabularInline):
	model = Customer
	raw_id_fields = ['clinic']
	extra=0
	class Meta:
		verbose_name = 'Pet Owner'
class ClinicAdmin(admin.ModelAdmin):
	fields = ('clinic_name','email', 'address', 'city','postal_code', 'user')
	list_display = ['clinic_name','email', 'address', 'city','postal_code']
	inlines = [PractitionerItemInline, NurseItemInline, CustomerItemInline]
###PHARMACY####
class PharmacistItemInline(admin.TabularInline):
	model = Pharmacist
	raw_id_fields = ['pharmacy_name']
	extra=0
class TechnicianItemInline(admin.TabularInline):
	model = Technician
	raw_id_fields = ['pharmacy']
	extra=0
class PharmacistAdmin(admin.ModelAdmin):
	fields = ('pharmacy_name','email', 'address', 'city','postal_code','user')
	list_display = ['pharmacy_name','email', 'address', 'city','postal_code']
	inlines = [PharmacistItemInline,TechnicianItemInline]

admin.site.register(ClinicGroup, GroupAdmin)
admin.site.register(Clinic, ClinicAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Pharmacy, PharmacistAdmin)
admin.site.register(Pet)


