from django.contrib import messages
from django.shortcuts import (
    render, get_object_or_404, redirect
)

from shop_place.forms import AddShopPlaceForm
from shop_place.models import ShopPlace


def AddShopPlaceView(request):
    data = {
        'form': AddShopPlaceForm()
    }
    if request.method == 'POST':
        form_shop_place = AddShopPlaceForm(data=request.POST)
        if form_shop_place.is_valid():
            form_shop_place.save()
            messages.success(request, 'El lugar se ha guardado exitosamente')
            return redirect(to='ShopPlaces')
    return render(request, 'shop_places/addPlace.html', data)


def EditShopPlaceView(request, id):
    place = get_object_or_404(ShopPlace, id=id)
    data = {
        'form': AddShopPlaceForm(instance=place)
    }
    if request.method == 'POST':
        form_shop_place = AddShopPlaceForm(data=request.POST, instance=place)
        if form_shop_place.is_valid():
            form_shop_place.save()
            messages.success(request, 'El lugar se ha guardado exitosamente')
            return redirect(to='ShopPlaces')
    return render(request, 'shop_places/editPlace.html', data)


def DeleteShopPlaceView(request, id):
    place = get_object_or_404(ShopPlace, id=id)
    place.delete()
    messages.success(request, 'Lugar de compra borrado')
    return redirect(to='ShopPlaces')


def TableShopPlaceView(request):
    places = ShopPlace.objects.all()
    data = {
        'places': places
    }
    return render(request, 'shop_places/table_shop_places.html', data)
