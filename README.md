# 🛍️ QorapShop

**QorapShop** — это интернет-магазин на Django с удобным REST API, системой аутентификации по JWT, подключением платежной системы Stripe и поддержкой фоновой обработки заказов через Celery. Приложение включает функциональность корзины, избранных товаров и полный набор CRUD-операций для управления магазином.

---

## 🚀 Функциональность

- ✅ Регистрация и аутентификация пользователей (JWT / Session)
- 📁 CRUD для:
  - Продуктов
  - Категорий
  - Корзины
  - Избранных товаров
  - Заказов
  - Пользователей
- 📊 Панель администратора Django
- 🌐 REST API с использованием Django REST Framework
- ⚙️ Фоновая обработка заказов через Celery + Redis
- 💳 Интеграция с платежной системой Stripe
- 🛒 Корзина с гибкой логикой
- ❤️ Добавление и управление избранными товарами

---

## 🛠️ Технологии

- Python 3.12.4
- Django 5.1.7
- Django REST Framework
- PostgreSQL / SQLite
- Docker (в планах)
- Celery + Redis
- Stripe 12.0.0

---

## 📂 Структура проекта
<details> <summary>📁 Структура проекта</summary>
```text
QORAP/
├── qorapshop/         # Конфигурация проекта
├── user/              # Пользователи
├── shop/              # Категории и продукты
├── payment/           # Платежи (Stripe)
├── orders/            # Заказы
├── favorites/         # Избранные товары
├── cart/              # Корзина
├── static/            # Статические файлы
├── media/             # Загружаемые медиа-файлы
├── templates/         # HTML-шаблоны
├── .env               # Переменные окружения
├── requirements.txt   # Зависимости проекта
└── manage.py
```
<details> 
---

## ⚙️ Установка и запуск

### 🔧 Локально

1. Клонируйте репозиторий:

```bash
git clone https://github.com/Aqwarys/QorapShop-Django.git
cd QorapShop-Django
```
2. Создайте виртуальное окружение
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
3. Установите зависимости
```bash
pip install -r requirements.txt
```
4. Примените миграции
```bash
python manage.py migrate
python manage.py createsuperuser
```
5. Создайте суперпользователя
```bash
python manage.py createsuperuser
```
6. Запустите сервер
```bash
python manage.py runserver
```

## 🔑 Переменные окружения
### Создайте файл .env в корне проекта и добавьте в него следующее:
```txt
DEBUG=True
STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_API_VERSION=2022-08-01
```

## 🧪 Тестирование
Пока не добавлено.

## 🐳 Docker
Пока не добавлено. Планируется реализация Docker и Docker Compose для удобного деплоя.

## 📑 Документация API
Swagger и ReDoc будут добавлены на следующих этапах разработки.

**Автор:** [Alisher Gilmanov (@Aqwarys)](https://github.com/Aqwarys) · 📧 aqwaryss@gmail.com
