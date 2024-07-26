from .models import Category, carusol_model,Product

def category(request):
    cate = Category.objects.all()
    return {'cate':cate}

def carusol(request):
    carus = carusol_model.objects.all()
    return {'carus':carus}

# def product_view(request, id):
#     pro_obj = Product.objects.get(id=id)
#     return {'pro_obj': pro_obj}

# def product_all(request):
#     prod = Product.objects.all()
#     return {'prod':prod}

# def product_pupolar(request):
#     pupolar = Product.objects.filter(is_favorite=True)
#     return {'pupolar':pupolar}