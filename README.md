![workflow](https://github.com/dmitry-brezgunov/yamdb_final/workflows/yamdb-workflow/badge.svg)
# API YamDB
## Описание
API для базы данных отзывов YamDB. Учебный проект для Яндекс.Практикум

API позволяет создавать и регистрировать пользователей, получать и создавать отзывы, комментарии. 

Полная документация к API доступна по адресу <локальный сервер>/redoc 

Проект написан в команде с другими студентами Яндекс.Практикума. Я занимался написанием API для регистрации, авторизации и управлением пользователями. 

## Стек
API написан на Python с использованием фреймворков Django и Django Rest Framework. Авторизация по JWT токену с использованием библиотеки simple-jwt. Фильтрация запросов с использованием библиотеки django-filter.

## Установка
На локальном компьютере должен быть установлен Docker.

1. Склонировать данный репозиторий на свой локальный компьютер.
2. В директории api_yamdb создать файл .env и прописать в нем переменные окружения:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
DB_PASSWORD=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
3. В терминале в корневой директории приложения выполнить команду `docker-compose up`.
4. После запуска контейнера в новой вкладке терминала выполнить команду `docker container ls` и узнать id контейнера.
5. Перейти в контейнер выполнив команду `docker container exec -it <id контейнер> bash`.
6. Внутри контейнера выполнить команды `python manage.py makemigrations` и `python manage.py migrate`.
7. Создать суперпользователя командой `python manage.py createsuperuser`.
