# Squilla test task


### Как запустить сервис

#### Зависимости

* python 3.7

#### Настройки

> настройки находятся в squilla_test_task/settings/*

#### Заполнение базы
* экспортировать путь к настройкам: `export DJANGO_SETTINGS_MODULE=squilla_test_task.settings.development`
* миграция бд: `python manage.py migrate`
* заполнить данные: `python manage.py populate`

#### Запуск сервиса
* экспортировать путь к настройкам: `export DJANGO_SETTINGS_MODULE=squilla_test_task.settings.development`
* запустить сервис: `python manage.py runserver 8000`
> сервис будет доступен на 127.0.0.1:8000
>
> swagger будет доступен на 127.0.0.1:8000/swagger


#### Авторизация

* После заполнения базы будет доступен пользователь `test` с паролем `testtest`

* Для получения токена нужно сделать запрос к `/api/auth/token/` с пользовательскими данными

* Полученный `access` токен подставить в заголовок `Authorization` в формате `Bearer {access}`. Например `Authorization: Bearer some_access_token_value`

* Для обновления токена нужно сделать повторную авторизацию или отправить refresh токен методу `/api/auth/refresh/`

> Подробнее в swagger

#### Страницы

* Ресурс со страницами доступен на /api/page/

> Подробнее в swagger
