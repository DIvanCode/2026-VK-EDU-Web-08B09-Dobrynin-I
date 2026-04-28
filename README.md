# 2026-VK-EDU-Web-08B09-Dobrynin-I

## Переменные окружения
Проект сначала читает `.env`, затем по переменной `ENVIRONMENT` подгружает файл окружения, например:
- `ENVIRONMENT=local` -> `.env.local`
- `ENVIRONMENT=docker` -> `.env.docker`

В репозиторий коммитится только `.env.example` без секретов.

## Локальный запуск
1. Запустить локально PostgreSQL. Можно запустить в docker контейнере командой:
```bash
docker-compose up -d db
```
2. Создать `.env` и указать окружение:
```bash
echo "ENVIRONMENT=local" > .env
```
3. Создать и заполнить `.env.local` по шаблону `.env.example`.
4. Установить зависимости и запустить сервер:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Запуск через Docker Compose
1. Создать `.env` и указать окружение:
```bash
echo "ENVIRONMENT=docker" > .env
```
2. Создать и заполнить `.env.docker` по шаблону `.env.example`.
3. Запустить проект:
```bash
docker-compose up --build
```

## Страницы
- `http://127.0.0.1:8000/` - список новых вопросов
- `http://127.0.0.1:8000/hot/` - список лучших вопросов
- `http://127.0.0.1:8000/tag/bender/` - список вопросов по тегу
- `http://127.0.0.1:8000/question/1/` - страница вопроса со списком ответов
- `http://127.0.0.1:8000/ask/` - форма создания вопроса
- `http://127.0.0.1:8000/login/` - форма логина
- `http://127.0.0.1:8000/signup/` - форма регистрации
- `http://127.0.0.1:8000/profile/` - форма редактирования профиля
