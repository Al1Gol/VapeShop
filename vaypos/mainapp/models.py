from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=20)
    priority = models.PositiveSmallIntegerField(verbose_name='Приоритет')
    tag = models.CharField(verbose_name='Тэг', max_length=20, default='123', unique=True, blank=True)
    sub_menu = models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True)


class ProductItem(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=100)
    desript = models.CharField(verbose_name='Описание', max_length=5000)
    image = models.ImageField(verbose_name="Изображение", upload_to="products", blank=True) 
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField(verbose_name='Количество')
 