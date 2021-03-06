from django import forms
from django.contrib.auth.models import User
from .models import Order, OrderItem
from users.models import Customer
#from localflavor.us.forms import USZipCodeField
from django.forms.models import inlineformset_factory
from Product.models import Product, Sales_Packaging
import logging
class OrderItemInlineForm(forms.ModelForm):
    
    class Meta:
        model = OrderItem
        exclude = ('pet','doctor',)
        extra = 0
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logger = logging.getLogger("mylogger")
        #qs = OrderItem.objects.get(pk=self.instance)
        #logger.info(qs)
        self.fields['packaging'].queryset = Sales_Packaging.objects.all()
class OrderCreateForm(forms.ModelForm):
    #postal_code = USZipCodeField()
    class Meta:
        model = Order
        exclude = ('paid','customer','shipping_address')

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['address','postal_code','city',]