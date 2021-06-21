from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from orders.models import Order, OrderItem
from users.models import Customer
#from localflavor.us.forms import USZipCodeField
from django.forms.models import inlineformset_factory
from django.forms import inlineformset_factory

class RxCreateForm(forms.ModelForm):
    #postal_code = USZipCodeField()
    class Meta:
        model = Order
        exclude = ('paid','customer','shipping_address')

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class RxOrderItemUpdateForm(forms.ModelForm):
    
    class Meta:
        model = OrderItem
        fields = ('rx_written','doctor','pet',)

    rx_written = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

class RxAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int,
                                      label=_('Quantity'))
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

#class UserCreateForm(forms.ModelForm):
#    class Meta:
#        model = User
#        fields = ('first_name', 'last_name', 'email')

#class CustomerCreateForm(forms.ModelForm):
#    class Meta:
#        model = Customer
#        fields = ['address','postal_code','city',]