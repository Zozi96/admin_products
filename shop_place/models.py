from django.db import models


# Create your models here.
class ShopPlace(models.Model):
    name_place = models.CharField(
        max_length=100, unique=True, verbose_name='Nombre de la plaza')
    city = models.CharField(max_length=90, verbose_name='Ciudad')

    def __str__(self):
        return f'Nombre de la Plaza: {self.name_place} | Ciudad: {self.city}'

    class Meta:
        verbose_name = 'Lugar de Compra'
        verbose_name_plural = 'Lugares de Compra'
