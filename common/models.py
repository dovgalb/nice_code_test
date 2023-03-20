from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Warehouse(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()
    product = models.ManyToManyField('Product', through='WarehouseProduct')

    def __str__(self):
        return f'Склад - {self.name}'


# Todo округлить до 2 знака
# TODO назначить positive int и float
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveSmallIntegerField()
    clients = models.ManyToManyField('Client', through='ProductClient')

    def __str__(self):
        return f'Товар - {self.name}'


class Client(models.Model):
    name = models.CharField(max_length=50)
    warehouse = models.ManyToManyField(Warehouse, through='ClientWarehouse')

    def __str__(self):
        return f'Клиент - {self.name}'


class ClientWarehouse(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    distance = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'Связь CW - {self.client}, {self.warehouse}'


# TODO подумать как сделать так, чтобы при значении is_allowed=false, rate=Null и capacity = null
class WarehouseProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    is_allowed = models.BooleanField()
    rate = models.PositiveSmallIntegerField(blank=True)
    capacity = models.PositiveSmallIntegerField(blank=True, help_text='Ограничение кол-ва определенного товара на складе')

    def __str__(self):
        return f'Связь WhP - {self.product}, {self.warehouse}'


# TODO добавить изменения в drowio
class ProductClient(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'Связь PC - {self.client}, {self.product}'
