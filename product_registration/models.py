from django.db import models

from products.models import Product
from shop_place.models import ShopPlace


class ProductRegistration(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name='Agregue el producto comprado',
        on_delete=models.CASCADE
    )
    place = models.ForeignKey(
        ShopPlace,
        verbose_name='Lugar de compra',
        on_delete=models.CASCADE
    )
    price = models.DecimalField(
        verbose_name='Precio',
        max_digits=8,
        decimal_places=2,
        default=0.0
    )
    date = models.DateField(
        verbose_name='Fecha de Compra',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Registro del Producto Comprado'
        verbose_name_plural = 'Registros de Productos Comprados'

    def __str__(self):
        return f'{self.product} ' \
               f'{self.place} ' \
               f'{self.price} ' \
               f'{self.date}' \
               f'{self.created_at}'
