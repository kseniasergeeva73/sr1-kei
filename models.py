from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=80, verbose_name='Название продукта')

    object = models.Model

    def __str__(self):
        return self.product_name


class Meta:
    verbose_name = 'Продукт'
    verbose_name_plural = 'Продукты'


class Detail(models.Model):
    product_name = models.CharField(max_length=80, verbose_name='Наименование')
    description = models.TextField(max_length=80, verbose_name='Описание')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    object = models.Model

    def __str__(self):
        return self.product_name


class Meta:
    verbose_name = 'Деталь'
    verbose_name_plural = 'Детали'


class Customer(models.Model):
    product_name = models.CharField(max_length=80, verbose_name='Наименование')
    goods = models.CharField(max_length=80, verbose_name='Товары')

    object = models.Model

    def __str__(self):
        return self.product_name


class Meta:
    verbose_name = 'Заказчик'
    verbose_name_plural = 'Заказчики'
# Create your models here.
