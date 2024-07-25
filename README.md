# Django tree menu for АпТрейдер (UpTrader)

## Установка
1. **Клонируйте репозиторий:**
   ```sh
   git clone https://github.com/SobrSergio/Django-tree_menu.git
   cd Django-tree_menu
   ```
2. **Создайте виртуальное окружение:**
   ```sh
   python -m venv env
   source env/bin/activate
   # для Windows `env\Scripts\activate`
   ```
3. **Примените миграции и создайте суперпользователя:**
   ```sh
   cd menu_tree
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Запустите сервер:**
   ```sh
   python manage.py runserver
   ```

Заполните базу данных через меню админов ("/admin") для проверки работоспособности меню.

