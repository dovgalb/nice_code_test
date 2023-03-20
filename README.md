# Тестовое задание для NiceCode
## Как запустить?
1. pip install -r requirements.txt (Устанавливаем зависимости)
2. make migration (выполняет команду python manage.py makemigrations)
3. make migrate  (выполняет применение миграций)
4. далее запускаем файл my_test_task/script.py, который запускает скрипт выполнения программы

(При каждом запуске скрипта из БД будут удаляться все созданные клиенты, товары и склады для более легкого отслеживания записей)

## Схемы
В my_test_task/dashboards хранятся PDF-файлы и файл .drawio 
в которых описана логика для связанных таблиц и логика алгоритма

Схема БД - https://github.com/dovgalb/nice_code_test/blob/main/dashboards/logics_db.drawio.pdf

Схема Алгоритма - https://github.com/dovgalb/nice_code_test/blob/main/dashboards/algoritm.drawio.pdf

## Принцип работы script.py

Функция create_entityamount: int, table: ModelBase, *args, **kwargs) создает сущности и
генерирует для них случайные значения на основе моделей

Далее скрипт создает 
1. Указанное кол-во товаров
2. Указанное кол-во складов
3. Указанное кол-во рандомных связей **склад_продукт** среди уже созданных товаров и складов, так же генерируются 
4. тарифы, максимальное кол-во товара на этом складе, и может ли он храниться на этом складе (у каждого склада могут 
5. быть только его продукты)
6. Указанное кол-во рандомных клиентов 
7. Указанное кол-во рандомных связей **клиент_продукт** среди уже созданных клиентов и товаров, так же генерируется 
8. кол-во приобретенного клиентом товара 
9. Указанное кол-во рандомных связей **клиент_склад** среди уже созданных клиентов и складов, так же генерируется 
10. дистанция от клиента склада (У каждого клиента могут быть только свои товары)

#### Функция возвращает список клиентов 
#### В моделях были переопределены и дополнены M2M связи [**склад_продукт**, **клиент_продукт**, **клиент_склад** ] т.к. 
1. тарифы
2. дистанция
3. максимальное хранимое кол-во товара для каждого склада
4. может ли конкретный товар храниться на конкретном складе или нет
5. кол-во заказанного клиентом товара
6. дистанция от склада до клиента с конкретным набором товаров

**Если рассуждать логично, то в БД может храниться только, действительно, существующая такая связь**

Я считаю, что связи между таблицами должны быть именно M2M, 
но при таком условии невозможно для них переопределить метод **save()**. 
В связи c чем мы не можем одновременно проверить общий лимит 
склада и потоварный лимит.

#### Была продумана принципиальная схема алгоритма
Но из-за проблемы с переопределением save() не вижу смысла дальнейшего написания заранее не работающего алгоритма 
В папке dashboards лежат pdf схемы алгоритма и БД(сначала рисовалась схема, а по ней уже модели)
https://github.com/dovgalb/nice_code_test/blob/main/dashboards/algoritm.drawio.pdf









