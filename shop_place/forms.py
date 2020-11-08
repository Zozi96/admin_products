from django import forms

from shop_place.models import ShopPlace


class AddShopPlaceForm(forms.ModelForm):
    class Meta:
        model = ShopPlace
        fields = '__all__'
