# ursip_test

Порядок запуска:

установка зависимостей

pip install -r requirements.txt


* применение миграций

python manage.py migrate


* создание пользователя для входа в админку

python manage.py createsuperuser


* применение скрипта выгрузки из excel файла

python manage.py load_from_excel  


* запуск сервера для просмотра админки

python manage.py runserver


* после этого должны появиться 2 таблицы

одна с исходными данными
http://localhost:8000/admin/data_analysis/analysis/

и вторая с суммами данных сгруппированных по дате
http://localhost:8000/admin/data_analysis/analysissumbydate/
