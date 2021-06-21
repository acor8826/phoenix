from django.contrib import admin
from .models import Order, OrderItem, ShippingAddress
class OrderItemInline(admin.TabularInline):
    fields = ('rx_written','product','packaging','pet','doctor','price','quantity','tax','tot_cost')
    model = OrderItem
    raw_id_fields = ['product']
    extra = 0
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	fields = ('customer','shipping_address','order_id')
	list_display = ['id','created', 'updated']
	list_filter = ['paid', 'created', 'updated']
	inlines = [OrderItemInline]

# Register your models here.
admin.site.register(ShippingAddress)