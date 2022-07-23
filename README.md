# YamDB CI/CD

![yamdb workflow](https://github.com/isBlueTip/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Описание

Проект по контейнеризации и автоматическому деплою YamDB с использованием Docker-compose, Nginx и Gunicorn. Новый коммит, запушенный на github, автоматически тестируется на соответствие PEP8 и проходит тесты. В случае успеха, новый код упаковывается в docker-образ, отправляется на docker hub, а затем автоматически скачивается и разворачивается удалённым сервером.

## Установка проекта

Необходимо создать форк репозитория и клонировать его на локальную машину. Для корректной работы, в папке `infra` необходимо создать файл .env с локальными переменными окружения, пример которого приведён ниже. Также нужно заполнить github secrets. Далее приведён список переменных окружения github:
```
DOCKER_USERNAME - логин docker hub
DOCKER_PASSWORD - пароль docker hub
HOST - IP удалённого сервера
USER - username удалённого сервера
SSH_KEY - приватный ключ ssh
PASSPHRASE - локальный пароль для доступа к ssh
```

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