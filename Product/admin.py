from django.contrib import admin
from .models import Category, Product, Product_Line, Sales_Packaging


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}

class ProductItemInline(admin.TabularInline):
	model = Product_Line
	raw_id_fields = ['linked_product']
	extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','form','slug','available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['available']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name','form',]
    filter_horizontal = ('packaging',)
    inlines = [ProductItemInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Sales_Packaging)



# Register your models here.
    
