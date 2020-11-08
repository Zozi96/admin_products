from django.db import models

from products.models import Product
from shop_place.models import ShopPlace


class ProductRegistration(models.Model):
    product = models.ForeignKey(Product, verbose_name='Agregue el producto comprado', null=False, blank=False,
                                on_delete=models.CASCADE)
    place = models.ForeignKey(ShopPlace, verbose_name='Lugar de compra', null=False, blank=False,
                              on_delete=models.PROTECT)
    price = models.DecimalField(verbose_name='Precio', null=False, blank=False, max_digits=8, decimal_places=2,
                                default=0.0)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} {self.place} {self.price} {self.created_at}'

    class Meta:
        verbose_name = 'Registro del Producto Comprado'
        verbose_name_plural = 'Registros de Productos Comprados'
