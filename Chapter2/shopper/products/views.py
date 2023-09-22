from django.shortcuts import get_object_or_404, render

from . models import Product
# Create your views here.
def home(request):
    return render(request, 'home.html')

def products(request):
    products = Product.objects.all()

    return render(request, 'products.html', {'products':products})


def detail(request, id, slug):
    product = get_object_or_404(Product, 
                                pk=id,
                                slug=slug,
                                )

    return render(request, 'detail.html', {'product':product})