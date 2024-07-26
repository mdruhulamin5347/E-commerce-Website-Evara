from django.shortcuts import render
from .models import Product
from django.shortcuts import render, get_object_or_404

# Create your views here.




def Product_details(request,id):
    obj = Product.objects.get(id=id)
    return render(request, 'product/product_details.html', {'obj': obj})
