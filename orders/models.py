from django.db import models
from django.contrib.auth.models import User
from Product.models import Product, Sales_Packaging
from users.models import Clinic, Customer, Pet, Practitioner
from django.db.models.signals import post_save, pre_save, pre_init
from django.dispatch import receiver
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
import datetime
#class Client(models.Model):
#    clinic = models.OneToOneField(Clinic, on_delete=models.CASCADE, blank=True,null=True)
#    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, blank=True, null=True)
    
#    @receiver(post_save, sender=Customer)
#    def create_client(sender, instance, created, **kwargs):
#        if created:
#            Client.objects.create(customer=instance)

#    @receiver(post_save, sender=Clinic)
#    def create_client(sender, instance, created, **kwargs):
#        if created:
#            Client.objects.create(clinic=instance)

#    def __str__(self):
#        if self.customer:
#            return str(self.customer)
#        if self.clinic:   
#            return str(self.clinic)

class ShippingAddress(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=250)
    zip_code = models.CharField(max_length=20)
    suburb = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id)

class Order(models.Model):
    order_id = models.CharField(max_length=100, blank=True, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        ordering = ('-created',)
    
  
    def __str__(self):
        return f'Order {self.id}'
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    
class OrderItem(models.Model):
    rx_written = models.DateField(default=datetime.date.today)
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)   
    doctor = models.ForeignKey(Practitioner, on_delete=models.CASCADE, blank=True, null=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1, blank=True, null=True)
    tot_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE, blank=True, null=True)
    packaging = models.ForeignKey(Sales_Packaging, on_delete=models.CASCADE, blank=True,null=True)
    def __str__(self):
        return '{}'.format(self.id)



    #####override save method #####    
    def save(self, *args, **kwargs):
        self.price = self.product.price
        self.tot_cost = self.product.price * self.quantity
        super(OrderItem, self).save(*args, **kwargs)

    @receiver(post_save, sender=Order)
    def set_tot_cost(sender, instance,**kwargs):
        for i in instance.items.all():
            price = i.product.price
            set_tot_cost = i.product.price * i.quantity
            tot_tax = set_tot_cost/11
            OrderItem.objects.update(price=price,tot_cost=set_tot_cost, tax=tot_tax)
    

        

# Create your models here.
