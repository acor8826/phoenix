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
from users.models import Clinic
def script_detail(request):
    cart = Cart(request)
    instance = request.session.session_key
    order_id = str(request.session.session_key)
    Order.objects.get_or_create(customer=request.user,order_id=instance)
    order = Order.objects.get(order_id =request.session.session_key)
    orderitem = OrderItem.objects.filter(order=order)
    user= request.user
    clinic = Clinic.objects.get(user=user)
    for item in cart:
        OrderItem.objects.update_or_create(order=order,
            product=item['product'],
            price=item['price'],
            quantity=item['quantity'])
    if request.method == 'POST':
        update_form = RxOrderItemUpdateForm(request.POST)
        if update_form.is_valid():
            form = update_form.save(commit=false)
            form.save()
        cart.clear()
        #request.session.delete()
        return render(request, 'order/created.html', {'update_form':update_form})
    else:
        update_form = RxOrderItemUpdateForm()
    return render(request, 'prescription/detail.html', {'orderitem':orderitem,'order':order,'order_id':order_id,'clinic':clinic,'user':user, 'cart':cart})
    #return render(request, 'prescription/detail.html', {'order_id':order_id,'clinic':clinic,'user':user, 'cart':cart,'form':form})
    #coupon_apply_form = CouponApplyForm()

    #r = Recommender()
    #cart_products = [item['product'] for item in cart]
    #recommended_products = r.suggest_products_for(cart_products, max_results=4)


