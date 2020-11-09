from django.contrib import admin
from django.urls import path

from admin_products.views import index_view

from product_registration.views import (
    AddRegistryView, TableRegistrationView, DeleteRegistryView, EditRegistryView
)

from products.views import (
    AddProducts, TableProducts, EditProductView, DeleteProductView
)

from shop_place.views import (
    AddShopPlaceView, TableShopPlaceView, EditShopPlaceView, DeleteShopPlaceView
)

urlpatterns = [
    path('', index_view, name='index'),
    path('admin/', admin.site.urls),

    path('shop-places/add-place', AddShopPlaceView, name='add_ShopPlaces'),
    path('edit/<id>', EditShopPlaceView, name='edit_ShopPlaces'),
    path('delete/<id>', DeleteShopPlaceView, name='delete_ShopPlaces'),
    path('shop-places/table-places', TableShopPlaceView, name='ShopPlaces'),

    path('products/add-products', AddProducts, name='add_Products'),
    path('edit/<id>', EditProductView, name='edit_Products'),
    path('delete/<id>', DeleteProductView, name='delete_Product'),
    path('products/table-products', TableProducts, name='Products'),

    path('registration/add-registry', AddRegistryView, name="add_Registry"),
    path('edit/<id>', EditRegistryView, name='edit_Registry'),
    path('delete/<id>', DeleteRegistryView, name='delete_Registry'),
    path('registration/table-registry', TableRegistrationView, name='Registration'),

]
