"""admin_products URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from admin_products.views import index_view
from product_registration.views import AddRegistryView, TableRegistrationView, DeleteRegistryView, EditRegistryView
from products.views import AddProducts, TableProducts, EditProductView, DeleteProductView
from shop_place.views import AddShopPlaceView, TableShopPlaceView, EditShopPlaceView, DeleteShopPlaceView

urlpatterns = [
    path('', index_view, name='index'),
    path('admin/', admin.site.urls),

    path('shop_places/addPlace', AddShopPlaceView, name='add_ShopPlaces'),
    path('edit/<id>', EditShopPlaceView, name='edit_ShopPlaces'),
    path('delete/<id>', DeleteShopPlaceView, name='delete_ShopPlaces'),
    path('shop_places/table_places', TableShopPlaceView, name='ShopPlaces'),

    path('products/addProducts', AddProducts, name='add_Products'),
    path('edit/<id>', EditProductView, name='edit_Products'),
    path('delete/<id>', DeleteProductView, name='delete_Product'),
    path('products/table_products', TableProducts, name='Products'),

    path('registration/addRegistry', AddRegistryView, name="add_Registry"),
    path('edit/<id>', EditRegistryView, name='edit_Registry'),
    path('delete/<id>', DeleteRegistryView, name='delete_Registry'),
    path('products/table_products', TableRegistrationView, name='Registration'),

]
