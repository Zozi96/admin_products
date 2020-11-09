from django.db import models


class Product(models.Model):
    name_product = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Nombre del producto'
    )

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f'{self.name_product}'
