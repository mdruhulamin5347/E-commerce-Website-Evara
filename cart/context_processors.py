from .models import add_to_cart

def added_cart(request):
    user = request.user
    cart = None
    total_amount = None
    sub_total = None
    if user.is_authenticated:
        cart = add_to_cart.objects.filter(user=user)
        for i in cart:
            i.quantity_subtotal = i.quantity * i.product.new_price

  
        sub_total = sum(item.product.new_price * item.quantity for item in cart)
        Shipping = 0
        total_amount = sub_total + Shipping
    return {'cart': cart,'total_amount':total_amount,'sub_total':sub_total}

