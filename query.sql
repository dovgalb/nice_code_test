
select
    client.id as client_id,
    client.name as client_name,
    client_product.product_id,
    client_product.amount as product_amount,
    cw.warehouse_id,
    cw.capacity as product_capacity,
    cw.is_allowed,
    c.capacity as warehouse_capacity
/*Тянем данные по клиентам из таблицы клиентов*/
from common_client as client
/*Джоиним таблицу КлиентПродукты, чтобы узнать получить продукты для каждого пользователя*/
left join common_productclient client_product on client.id = client_product.client_id
/*Джоиним таблицу СкладПродукт, чтобы узнать какие товары в каких складах могут располагаться*/
left join common_warehouseproduct cw on client_product.product_id = cw.product_id
/*Джоиним таблицу Склады, чтобы узнать общую вместимость складов*/
left join common_warehouse c on cw.warehouse_id = c.id

