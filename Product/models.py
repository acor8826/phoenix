from django.db import models
from decimal import Decimal
from inventory.models import Active
from list.models import Form, Unit, Target_Species
from inventory.models import Packaging
from formulary.models import Formula
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save
from django.db.models.signals import post_save
from django.urls import reverse
from slugify import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])

        
    def __str__(self):
        return self.name

class Sales_Packaging(models.Model):
    short_desc = models.CharField(max_length=255, null=True, blank=True)
    inventory_item = models.ForeignKey(Form, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        ordering = ('short_desc',)
        verbose_name = 'Packaging'
        verbose_name_plural = 'Packaging'
    
    def __str__(self):
        return str(self.short_desc)        

class Product(models.Model):
    formula = models.ForeignKey(Formula,
                                 related_name='formula',
                                 on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True, null=True, blank=True)
    form = models.ForeignKey(Form, on_delete=models.CASCADE, null=True, blank=True)
    target_species = models.ForeignKey(Target_Species, on_delete=models.CASCADE, null=True, blank=True)
    packaging = models.ManyToManyField(Sales_Packaging, blank=True)
    slug = models.SlugField(max_length=200, db_index=True, null=True, blank=True)
    image = models.ImageField(upload_to='product_img/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    qty = models.IntegerField(blank=True, null=True, default=0) 
    available = models.BooleanField(default=True)
    #compound = models.BooleanField(default=True)
    GST = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
   
    #def __str__(self):
    #    return str("%s (%s)" % (self.name,", ".join(Sales_Packaging.short_desc for sales_packaging in self.sales_packagings.all()),))
    
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])


    def get_name(self):
        for item in self.product_line_set.all():
            name = str(item.active) +str(" ")+str(item.strength)+str(" ")+str(item.UoM) + str(qty)+str(" ")++str("in")++str(" ")+str(packaging)
        return name

    def __str__(self):
        return str(self.name)
    #####override save method #####    
    def save(self, *args, **kwargs):
        self.slug=slugify(str(self.name)+str(" ")+str(self.form)+str(" ")+str(self.qty)+str(" "))
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name) + str(" ") + str(self.form) + str(" ") +  str(self.qty)

class Product_Line(models.Model):
    linked_product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True, blank=True)
    active = models.ForeignKey(Active, on_delete=models.CASCADE, null=True, blank=True)
    strength = models.IntegerField(default=0, null=True, blank=True)
    UoM = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, db_index=True, default=True, blank=True)
    class Meta:
        ordering = ['linked_product']

    
    def save(self, *args, **kwargs):
        self.name = str(self.active) + str(" ") + str(self.strength)+ str(" ") + str(self.UoM)
        self.linked_product.name = (str(self.linked_product.name) + str(" ")+str(self.name)).replace("None","")
        #self.linked_product.slug = slugify(str(self.linked_product.name)) // I think this needs to go on the Product Method
        self.linked_product.save()
        super(Product_Line, self).save(*args, **kwargs)



