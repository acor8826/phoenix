from django.contrib import admin
from .models import Order, OrderItem, ShippingAddress
from Product.models import Product, Sales_Packaging
from .forms import OrderItemInlineForm
import logging

class OrderItemInline(admin.TabularInline):
	#fields = ('rx_written','product','packaging','pet','doctor','price','quantity','tax','tot_cost')
	model = OrderItem
	form = OrderItemInlineForm
	extra = 0
	#def get_formset(self, request, obj=None, **kwargs):
	#	OrderItemInline.obj = obj
	#	return super(OrderItemInline, self).get_formset(request, obj, **kwargs)

	#def formfield_for_foreignkey(self, db_field, request, **kwargs):
	#	if db_field.name == "packaging":
	#		try:
	#			logger = logging.getLogger("mylogger")
	#			for i in Product.objects.all():
	#				pack = i.packaging.all()
	#				for qs in pack:
	#					name = qs.short_desc
	#					logger = logging.getLogger("mylogger")
	#					logger.info(name)
	#			kwargs["queryset"] = Sales_Packaging.objects.filter(short_desc__in=['1 box', '500ml Tub'])
	#		except IndexError:
	#			logger = logging.getLogger("mylogger")
	#			logger.info('error')
	#			pass
	#	return super().formfield_for_foreignkey(db_field, request, **kwargs)		
  
        
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	fields = ('customer','shipping_address','order_id')
	list_display = ['id','created', 'updated']
	list_filter = ['paid', 'created', 'updated']
	inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItem(admin.ModelAdmin):
	model = OrderItem
	fields = ['rx_written','product','packaging','pet','doctor','price','quantity','tax','tot_cost']
	list_select_related= ['packaging',]


admin.site.register(ShippingAddress)