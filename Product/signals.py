from django.db.models.signals import post_save
from .models import Product, Product_Line

def update_parent(sender, instance, created, **kwargs):
	post_save.connect(update_parent, send =Product_Line)