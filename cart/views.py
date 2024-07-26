from django.shortcuts import render,redirect
from .models import add_to_cart
from product.models import Product
from django.contrib.auth.decorators import login_required
from accounts.models import my_address
# Create your views here.

def add_cart(request, id):
    user = request.user
    if user.is_authenticated:
        prod = Product.objects.get(id=id)
        try:
            cart = add_to_cart.objects.get(user=user, product=prod)
            cart.quantity += 1
            cart.save()
        except add_to_cart.DoesNotExist:
            add_to_cart.objects.create(user=user, product=prod)
    return redirect(request.META.get('HTTP_REFERER'))



@login_required
def Check_out(request):
    user = request.user
    billing_address = my_address.objects.filter(user=user, id=1).first()
    shiping_address = my_address.objects.filter(user=user, id=2).first()
    
    return render(request, 'cart/check_out.html', {'billing_address': billing_address,'shiping_address': shiping_address,})


def Shop_cart(request):
    return render(request, 'cart/shop_cart.html')

def shop_cart_item_remove(request,id):
    remove_item = add_to_cart.objects.get(id=id)
    remove_item.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def shop_cart_item_clear(request):
    clear_item = add_to_cart.objects.all()
    clear_item.delete()
    return redirect(request.META.get('HTTP_REFERER'))


