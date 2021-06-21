from django.urls import path
#from .views import ProductDetailView, Update_Purchase, All_Product, ProductCategory, ProductSpecial
from django.conf.urls import url 
from . import views
from .models import *
app_name = 'shop'
urlpatterns = [
     path('',views.home, name="home"),
     path('', views.product_list, name='product_list'),
     path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
     path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]
