# Тестовое задание для NiceCode
## Как запустить?
1. pip install -r requirements.txt (Устанавливаем зависимости)
2. make migration (выполняет команду python manage.py makemigrations)
3. make migrate  (выполняет применение миграций)
4. run my_test_task/script.py (запускаем скрипт)

## Схемы
В my_test_task/dashboards хранятся PDF-файлы и файл .drawio 
в которых описана логика для связанных таблиц и логика алгоритма


## Принцип работы script.py


Функция create_entityamount: int, table: ModelBase, *args, **kwargs) создает сущности и генерирует для них случайные значения на основе моделей





