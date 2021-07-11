from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from Product.models import Product
from cart.cart import Cart
from cart.forms import CartAddProductForm
from orders.forms import OrderCreateForm
from orders.models import Order, OrderItem
from .forms import RxCreateForm, RxAddProductForm, RxOrderItemUpdateForm
#from coupons.forms import CouponApplyForm
#from shop.recommender import Recommender
from django.forms import inlineformset_factory
from django.forms import formset_factory
from users.models import Clinic, Customer
def script_detail(request):
    cart = Cart(request)
    ###querysets####
    instance = request.session.session_key
    order_id = str(request.session.session_key)
    Order.objects.get_or_create(customer=request.user,order_id=instance)
    order = Order.objects.get(order_id =request.session.session_key)
    orderitem = OrderItem.objects.filter(order=order)
    user= request.user
    clinic = Clinic.objects.get(user=user)
    pet_owner, created = Customer.objects.get_or_create(clinic=clinic)
###INLINE FORM####
    OrderFormSet = inlineformset_factory(Order, OrderItem, fields=('order',
        'rx_written','pet','doctor','product','price','quantity','tot_cost','tot_cost','packaging', ), extra=0)
    order = Order.objects.get(order_id=instance)
    formset= OrderFormSet(instance=order)
    #####CART####
    for item in cart:
        OrderItem.objects.update_or_create(order=order,
            product=item['product'],
            price=item['price'],
            quantity=item['quantity'])
    if request.method == 'POST':
        #update_form = RxOrderItemUpdateForm()
        formset = OrderFormSet(request.POST, instance=order)
        if formset.is_valid():
            formset.save()
            cart.clear()
        #request.session.delete()
        return render(request, 'order/created.html', {'formset':formset})
    else:
        update_form = RxOrderItemUpdateForm()
    return render(request, 'prescription/detail.html', {'formset':formset,'pet_owner':pet_owner,'orderitem':orderitem,'order':order,'order_id':order_id,'clinic':clinic,'user':user, 'cart':cart})
    #return render(request, 'prescription/detail.html', {'order_id':order_id,'clinic':clinic,'user':user, 'cart':cart,'form':form})
    #coupon_apply_form = CouponApplyForm()

    #r = Recommender()
    #cart_products = [item['product'] for item in cart]
    #recommended_products = r.suggest_products_for(cart_products, max_results=4)


