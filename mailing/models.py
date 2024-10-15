from time import localtime

from django.db import models
from django.utils import timezone

from nullable import NULLABLE

STATUS_CHOICES = [
    ('created', 'Создана'),
    ('active', 'Запущена'),
    ('finished', 'Завершена'),
]
INTERVAL_CHOICES = [
    ('once', 'разовая'),
    ('daily', 'ежедневно'),
    ('weekly', 'раз в неделю'),
    ('monthly', 'раз в месяц'),
]
ACTIVE_CHOICES = [
    (True, 'Активна'),
    (False, 'Неактивна'),
]
LOG_CHOICES = [
    (True, 'Успешно'),
    (False, 'Неудача'),
]


class Client(models.Model):
    name = models.CharField(max_length=150, verbose_name='ФИО')
    email = models.EmailField(unique=True, verbose_name='Почта')
    commentary = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Message(models.Model):
    topic = models.CharField(max_length=250, verbose_name='Тема')
    content = models.TextField(verbose_name='Содержание')

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Mailing(models.Model):
    name = models.CharField(max_length=50, verbose_name='Рассылка')
    mail_to = models.ManyToManyField(Client, verbose_name='Получатели')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение', **NULLABLE)
    start_date = models.DateTimeField(default=localtime, verbose_name='Начало рассылки')
    next_date = models.DateTimeField(default=localtime, verbose_name='Следующая рассылка')
    end_date = models.DateTimeField(verbose_name='Конец рассылки')
    interval = models.CharField(default='once', max_length=10, choices=INTERVAL_CHOICES, verbose_name='Периодичность')
    status = models.CharField(default='created', max_length=10, choices=STATUS_CHOICES, verbose_name='Статус')
    is_activated = models.BooleanField(default=True, choices=ACTIVE_CHOICES, verbose_name='Активность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('start_date',)


class Logs(models.Model):
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка', **NULLABLE)
    last_datetime_sending = models.DateTimeField(auto_now=True, verbose_name='Время рассылки', **NULLABLE)
    status = models.CharField(default=False, max_length=30, choices=LOG_CHOICES, verbose_name='Попытка', **NULLABLE)

    def __str__(self):
        return f'{self.last_datetime_sending} - {self.status}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
