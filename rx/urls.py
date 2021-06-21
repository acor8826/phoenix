from django.urls import path
from . import views
app_name = 'script'
urlpatterns = [
    path('', views.script_detail, name='script_detail'),
    #path('add/<int:product_id>/', views.script_detail, name='cart_add'),
    #path('remove/<int:product_id>/', views.cart_remove, 
                                     #name='cart_remove'),
]