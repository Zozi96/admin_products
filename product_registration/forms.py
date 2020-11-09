from django import forms

from product_registration.models import ProductRegistration


class RegistryForm(forms.ModelForm):
    class Meta:
        model = ProductRegistration
        fields = '__all__'

        widgets = {
            'date': forms.SelectDateWidget()
        }
