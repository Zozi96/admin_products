from django.db import models


# Create your models here.
class ShopPlace(models.Model):
    name_place = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Nombre de la plaza'
    )

    class Meta:
        verbose_name = 'Lugar de Compra'
        verbose_name_plural = 'Lugares de Compra'

    def __str__(self):
        return f'{self.name_place}'
