from django.db import models


class Product(models.Model):
    name_product = models.CharField(
        max_length=255, unique=True, verbose_name='Nombre del producto')

    def __str__(self):
        return f'Nombre del producto: {self.name_product}'

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
