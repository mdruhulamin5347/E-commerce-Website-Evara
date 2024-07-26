from django.shortcuts import render
from product.models import Product
# Create your views here.
def HOME(request):
    prod = Product.objects.all()
    featured = Product.objects.filter(is_featured=True)
    popular = Product.objects.filter(is_popular=True)
    newadded = Product.objects.filter(is_newadded=True)
    context = {
        'prod':prod,
        'featured':featured,
        'popular':popular,
        'newadded':newadded
    }
    return render(request,'home/home.html',context)