from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from sslcommerz_lib import SSLCOMMERZ
from cart.models import add_to_cart

def Order_payment(request):
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

    settings = {'store_id': 'testbox', 'store_pass': 'qwerty', 'issandbox': True}
    sslcommez = SSLCOMMERZ(settings)
    
    post_body = {
        'total_amount': total_amount,
        'currency': "BDT",
        'tran_id': "12345",
        'success_url': "http://127.0.0.1:8000/payment-success/",
        'fail_url': "http://127.0.0.1:8000/payment-fail/",
        'cancel_url': "your cancel url",
        'emi_option': 0,
        'cus_name': "test",
        'cus_email': "test@test.com",
        'cus_phone': "01700000000",
        'cus_add1': "customer address",
        'cus_city': "Dhaka",
        'cus_country': "Bangladesh",
        'shipping_method': "NO",
        'multi_card_name': "",
        'num_of_item': 1,
        'product_name': "Test",
        'product_category': "Test Category",
        'product_profile': "general"
    }

    response = sslcommez.createSession(post_body)
    return redirect(response['GatewayPageURL'])

@csrf_exempt
def Payment_success(request):
    return render(request, 'order/payment_succes.html')

@csrf_exempt
def Payment_fail(request):
    return render(request, 'order/payment_fail.html')