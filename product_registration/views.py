from django.shortcuts import (
    render, redirect, get_object_or_404
)

from product_registration.forms import RegistryForm
from product_registration.models import ProductRegistration


def AddRegistryView(request):
    data = {
        'form': RegistryForm
    }
    if request.method == 'POST':
        form_add_product = RegistryForm(data=request.POST)
        form_add_product.save()
        return redirect(to='Registration')
    return render(request, 'product_registration/addRegistry.html', data)


def EditRegistryView(request, id):
    registry = get_object_or_404(ProductRegistration, id=id)
    data = {
        'form': RegistryForm(instance=registry)
    }
    if request.method == 'POST':
        form_shop_place = RegistryForm(data=request.POST, instance=registry)
        if form_shop_place.is_valid():
            form_shop_place.save()
            return redirect(to='Registration')
    return render(request, 'product_registration/editRegistry.html', data)


def DeleteRegistryView(request, id):
    registry = get_object_or_404(ProductRegistration, id=id)
    registry.delete()
    return redirect(to='Registration')


def TableRegistrationView(request):
    registros = ProductRegistration.objects.all()
    data = {
        'registros': registros
    }
    return render(request, 'product_registration/table_registration.html', data)
