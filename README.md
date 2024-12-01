# Сервис YaCut

## Описание проекта

**Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.**

## Установка и настройка

1. **Клонирование репозитория:**
    
    ```bash
    git clone git@github.com:closecodex/yacut.git
    cd yacut
    ```

2. **Создание и активация виртуального окружения:**

    ```bash
    python -m venv venv
    source venv\Scripts\activate
    ```

3. **Обновление менеджера пакетов и установка зависимостей:**
   
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Выполнение миграций:**
    
   ```bash
   flask db init
   flask db migrate -m "комментарий"
   flask db upgrade
   ```

5. **Запуск приложения:**

    ```bash
    flask run
    ```

## Примеры запросов

- POST /api/id/

    * Запрос: 
        ```json
        {
        "url": "https://www.example.com",
        "custom_id": "mycustomid" * (необязательное поле)
        }
        ```
    * Ответ:
        ```json
        {
        "url": "https://www.example.com",
        "short_link": "http://127.0.0.1:5000/mycustomid"
        }
        ```

- GET /api/id/<short_id>/

    * Ответ:
        ```json
        {
        "url": "https://www.example.com"
        }
        ```

## Дополнительная информация

1. **Автор: Мария Осмоловская (closecodex@github.com)**

2. **Технологии: Python, Flask 2.0, SQLAlchemy, Alembic (Flask-Migrate), PostgreSQL/SQLite**