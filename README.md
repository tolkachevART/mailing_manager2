# Сервис рассылки писем
## Описание
Данный сервис предназначен для упрощения процесса создания и управления email рассылками.
## Установка и запуск
1. **Установите зависимости**
2. **Определите необходимые переменные окружения**
3. **Сделайте миграции**:
  python manage.py makemigrations |
  python manage.py migrate
4. **Создайте суперпользователя**
   python manage.py сsu
5. **Запуск программы**
   python manage.py runserver
6. **Сервис автоматической рассылки**:
   python manage.py runapscheduler
7. **Redis**:
  sudo service redis-server start |
  redis-cli
    

