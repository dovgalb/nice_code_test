import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_test_task.settings")
django.setup()
from django.db.models.base import ModelBase
from common.models import Product, Warehouse, WarehouseProduct, Client, ProductClient, ClientWarehouse
from mixer.backend.django import mixer

TRANSPORT_TAX: float = 0.01


def create_entity(amount: int, table: ModelBase, *args, **kwargs) -> list:
    return mixer.cycle(amount).blend(table, *args, **kwargs)


def insert_in_db() -> list["clients"]:
    # TODO find method to clear DB
    Product.objects.all().delete()
    Warehouse.objects.all().delete()
    Client.objects.all().delete()

    # создаем рандомные продукты
    products = create_entity(2, Product)
    # создаем рандомные склады
    warehouse = create_entity(3, Warehouse)
    # создаем рандомные связи склады-продуктыы
    warehouse_product = create_entity(3, WarehouseProduct, product=mixer.SELECT, warehouse=mixer.SELECT)

    # создаем рандомных клиентов
    clients = create_entity(3, Client)
    # создаем связи клиент продукт
    client_product = create_entity(3, ProductClient, product=mixer.SELECT, client=mixer.SELECT)
    # создаем связи клиент склад
    client_warehouse = create_entity(2, ClientWarehouse, warehouse=mixer.SELECT, client=mixer.SELECT)
    # print(clients)
    return clients


def count_something(clients):
    for client in clients:
        products = ProductClient.objects.filter(client_id=client.id)
        print(products.values())
        # warehouses = WarehouseProduct.objects.filter(product_id__in=products)










def main():
    clients = insert_in_db()
    count_something(clients)


# TODO добавить логгирование чтобы информация шла в консоль
# TODO закончить бизнес логику
# TODO напоминание проверяй когда будешь производить расчеты поле is_allowed
if __name__ == "__main__":
    main()
