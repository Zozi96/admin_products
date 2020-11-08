from django import forms

from products.models import Product


class RegistryForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['created_at']
