from django.shortcuts import (
    redirect, render, get_object_or_404
)

# Create your views here.
from products.forms import ProductForm
from products.models import Product


def AddProducts(request):
    data = {
        'form': ProductForm
    }
    if request.method == 'POST':
        form_add_product = ProductForm(data=request.POST)
        form_add_product.save()
        return redirect(to='Products')
    return render(request, 'products/addProducts.html', data)


def EditProductView(request, id):
    product = get_object_or_404(Product, id=id)
    data = {
        'form': ProductForm(instance=product)
    }
    if request.method == 'POST':
        form_shop_place = ProductForm(data=request.POST, instance=product)
        if form_shop_place.is_valid():
            form_shop_place.save()
            return redirect(to='Products')
    return render(request, 'products/editProducts.html', data)


def DeleteProductView(request, id):
    place = get_object_or_404(Product, id=id)
    place.delete()
    return redirect(to='Products')


def TableProducts(request):
    products = Product.objects.all()
    data = {
        'products': products
    }
    return render(request, 'products/table_products.html', data)
