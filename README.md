## Установка и запуск

### Создание venv

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

Установка зависимостей:
```bash
pip install -r requirements.txt
```

### Миграции

Применение миграций:
```bash
python manage.py migrate
```

### Запуск

```bash
python manage.py runserver
```

Суперпользователь (для админки):
```bash
python manage.py createsuperuser
```

## API

- **GET** `/api/clients/` — JSON со списком клиентов (id, ФИО, баланс, статус).
- Фильтр по статусу: `?status=lead` / `?status=client`. Без параметра — все клиенты.
