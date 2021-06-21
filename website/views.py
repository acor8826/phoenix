from django.shortcuts import render, get_object_or_404
from list.models import Target_Species
from Product.models import Category, Product, Product_Line
from cart.forms import CartAddProductForm
from cart.cart import Cart
def home(request):
    cart = Cart(request)
    category = Category.objects.all()
    product = Product.objects.all()
    target_species = Target_Species.objects.all()
    cart_product_form = CartAddProductForm()
    user = request.user
    return render(request, 'store/home.html', {
        'cart':cart,
		'user':user,
        'target_species':target_species,
		'category':category, 
		'product':product, 
		'cart_product_form': cart_product_form})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'store/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id,
                                         slug=slug,
                                         available=True)
    cart_product_form = CartAddProductForm()
    return render(request,'store/product-detail.html',{'product': product,'cart_product_form': cart_product_form})