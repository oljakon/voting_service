# voting_service


# Содержание

1. [Описание задачи](#Описание-задачи)
1. [Запуск](#Запуск)
1. [Тесты](#Тесты)
1. [Схема базы данных](#Схема-базы-данных)
1. [API](#API)


# Описание задачи

Нужно реализовать HTTP сервис для голосования. Например, для выбора самого популярного покемона. UI не нужен, достаточно сделать JSON API сервис. Должна быть возможность:

* Создать новое голосование с разными вариантами ответов
* Отдать свой голос за какой-либо вариант
* Получить текущий результат голосования

# Запуск

* Клонировать проект с репозитория GitHub
```
git clone https://github.com/oljakon/voting_service.git
```

* Перейти в директорию *voting_service*
```
cd voting_service/
```

* Запустить *docker_compose*
```
docker-compose up
```

# Тесты

* Запуск тестов
```
docker-compose run web ./manage.py test
```

* Процент покрытия тестами
```
docker-compose run web coverage run --source=api manage.py test
docker-compose run web coverage report
```

| Name          | Statements    | Missing       | Coverage      |
| ------------- | ------------- | ------------- | ------------- |
api/\_\_init\_\_.py |                 0 |     0 |  100% |
api/admin.py        |                 4 |     0 |  100% |
api/apps.py         |                 4 |     0 |  100% |
api/models.py       |                11 |     2 |   82% |
api/serializers.py  |                10 |     0 |  100% |
api/tests/\_\_init\_\_.py |           0 |     0 |  100% |
api/tests/test_models.py  |          33 |     0 |  100% |
api/tests/test_serializers.py |      28 |     0 |  100% |
api/tests/test_views.py   |          82 |     0 |  100% |
api/urls.py               |           3 |     0 |  100% |
api/views.py              |          42 |     0 |  100% |
Toltal                    |         223 |     2 |   99% |


# Схема базы данных

[Miro](https://miro.com/app/board/o9J_l-evOx8=/)


# API

Документация в формате Swagger находится по адресу: http://127.0.0.1:8000/api/

Тело запроса и ответа - в формате JSON.

В случае возникновения ошибки возвращается ее HTTP код и краткое описание.


## POST /api/createPoll/

Создание голосования с вариантами ответов.

* Тело запроса:
  * poll - параметры голосования,
    * name - название голосования,
  * choices - варианты голосования.
* Тело ответа:
  * id - id созданного голосования,
  * name - название созданного голосвания.

__Пример:__

Запрос:
```
```

Ответ:
```
```

