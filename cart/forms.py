
from django import forms
from django.utils.translation import gettext_lazy as _
from users.models import Practitioner


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
PRESCRIBER_CHOICES = Practitioner.objects.all()

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int,
                                      label=_('Quantity'))
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
class CartAddPresciberForm(forms.Form):
    prescriber = forms.ChoiceField(choices=PRESCRIBER_CHOICES)