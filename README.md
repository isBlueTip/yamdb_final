# YamDB CI/CD

![yamdb workflow](https://github.com/isBlueTip/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Описание

Проект по контейнеризации и автоматическому деплою YamDB с использованием Docker-compose, Nginx и Gunicorn. Новый коммит, запушенный на github, автоматически тестируется на соответствие PEP8 и проходит тесты. В случае успеха, новый код упаковывается в docker-образ, отправляется на docker hub, а затем автоматически скачивается и разворачивается удалённым сервером. Развёрнутый проект доступен по aдресу [www.yetanotheryatube.onthewifi.com/api/v1](http://yetanotheryatube.onthewifi.com/api/v1), документация - по [www.yetanotheryatube.onthewifi.com/redoc](http://yetanotheryatube.onthewifi.com/redoc)

[comment]: <> (## Установка проекта локально)

[comment]: <> (Необходимо создать форк репозитория и клонировать его на локальную машину. Для корректной работы, в папке `infra` необходимо создать файл .env с локальными переменными окружения, например:)

[comment]: <> (```)

[comment]: <> (DB_ENGINE=django.db.backends.postgresql)

[comment]: <> (DB_NAME=postgres)

[comment]: <> (POSTGRES_USER=postgres)

[comment]: <> (POSTGRES_PASSWORD=root)

[comment]: <> (DB_HOST=db)

[comment]: <> (DB_PORT=5432)

[comment]: <> (SECRET_KEY=?5FXk"ncyRbP#a<n94't%V&#40;&t_UmC`N9rC$7iW&#41;m#'ZUSak<5-#XoWX}N)

[comment]: <> (```)

[comment]: <> (Выполнить установку виртуального окружения и зависимостей:)

[comment]: <> (```bash)

[comment]: <> (python3 -m venv venv)

[comment]: <> (source venv/bin/activate)

[comment]: <> (pip install -r api_yamdb/requirements.txt)

[comment]: <> (```)

[comment]: <> (Далее, из папки `infra` выполнить:)

[comment]: <> (```bash)

[comment]: <> (docker-compose up --build -d)

[comment]: <> (```)

## Установка проекта на удалённый сервер

Необходимо создать форк репозитория и клонировать его на локальную машину. Заполнить github secrets. Далее приведён список необходимых переменных окружения github:
```
DB_ENGINE           - django.db.backends.postgresql
DB_HOST             - db
DB_NAME             - postgres
DB_PORT             - 5432
DOCKER_USERNAME     - логин docker hub
DOCKER_PASSWORD     - пароль docker hub
HOST                - IP удалённого сервера
USER                - username удалённого сервера
PASSPHRASE          - локальный пароль для доступа к ssh
SSH_KEY             - приватный ключ ssh
POSTGRES_PASSWORD   - логин docker hub
POSTGRES_USER       - имя пользователя для доступа к БД
SECRET_KEY          - код безопасности django-проекта
TELEGRAM_TO         - токен пользователя telegram
TELEGRAM_TOKEN      - токен бота telegram
```

Копировать файлы на сервер:
```bash
scp infra/docker-compose.yaml <HOST_USERNAME>@<HOST_IP>:~
```
Где HOST_USERNAME - имя пользователя на удалённом сервере,
HOST_IP - IP-адрес сервера
И выполнить push в ветку main. Развёрнутый проект будет доступен по IP-адресу сервера.

## Пример .env файла
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=pass
DB_HOST=db
DB_PORT=5432
SECRET_KEY=p&l%385148kslhtyn^##a1)ilzsdf8s6@4zqs&dfsdfsdf-sdfsd+dfq=l^##zgl9(vs
```

## Стек

Django, Django REST framework, Github Actions, Docker, JWT, Postgres, Nginx, Gunicorn

## Автор

Семён Егоров

[LinkedIn](https://www.linkedin.com/in/simonegorov/)  
[Email](rhinorofl@gmail.com)  
[Telegram](https://t.me/SamePersoon)