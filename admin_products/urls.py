from django.contrib import admin
from django.urls import path

from admin_products.views import index_view
from product_registration.views import (
    AddRegistryView, TableRegistrationView, DeleteRegistryView, EditRegistryView
)
from products.views import (
    AddProducts, TableProducts, EditProductView, DeleteProductView,
)
from shop_place.views import (
    AddShopPlaceView, TableShopPlaceView, EditShopPlaceView, DeleteShopPlaceView
)

urlpatterns = [
    path('', index_view, name='index'),
    path('admin/', admin.site.urls),

    # Shop Places
    path('shop-places/add-place', AddShopPlaceView, name='add_ShopPlaces'),
    path('shop-places/edit-shop-place/<id>', EditShopPlaceView, name='edit_ShopPlaces'),
    path('shop-places/delete-shop-place/<id>', DeleteShopPlaceView, name='delete_ShopPlaces'),
    path('shop-places/table-places', TableShopPlaceView, name='ShopPlaces'),

    # Products
    path('products/add-products', AddProducts, name='add_Products'),
    path('products/edit-product/<id>', EditProductView, name='edit_Products'),
    path('products/delete-product/<id>', DeleteProductView, name='delete_Product'),
    path('products/table-products', TableProducts, name='Products'),

    # Registration
    path('registration/add-registry', AddRegistryView, name="add_Registry"),
    path('registration/edit-registry/<id>', EditRegistryView, name='edit_Registry'),
    path('registration/delete-registry/<id>', DeleteRegistryView, name='delete_Registry'),
    path('registration/table-registry', TableRegistrationView, name='Registration'),

]
