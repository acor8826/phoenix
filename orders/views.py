from users.models import Customer
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm, CustomerCreateForm, UserCreateForm
from django.forms import modelformset_factory
from cart.cart import Cart

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        user_form = UserCreateForm(request.POST)
        customer_create_form = CustomerCreateForm(request.POST)
        if form.is_valid()and customer_create_form.is_valid():
            #Commit the form to get the data
            user = user_form.save(commit=False)
            customer =  customer_create_form.save(commit=False)
            order = form.save(commit=False)
            #Set the field value
            user.username = user.email.split('@')[0]
            user.save()
            Customer.objects.create(user=user, address=customer.address,postal_code=customer.postal_code, city=customer.city )
            order.customer = user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # clear the cart
            cart.clear()
            return render(request,
                          'order/created.html',
                          {'order':order,'customer':customer,'user':user})
    else:
        form = OrderCreateForm()
        user_form = UserCreateForm()
        customer_create_form = CustomerCreateForm()
    return render(request,
                  'order/create.html',
                  {'cart': cart, 
                  'form': form,
                  'customer_create_form':customer_create_form,
                  'user_form':user_form})


