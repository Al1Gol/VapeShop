from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=20)
    img = models.ImageField(verbose_name="Изображение", upload_to="products", blank=True) 
    priority = models.PositiveSmallIntegerField(verbose_name='Приоритет')


class ProductItem(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=100)
    desript = models.CharField(verbose_name='Описание', max_length=5000)
    img = models.ImageField(verbose_name="Изображение", upload_to="products", blank=True) 
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField(verbose_name='Количество')
 