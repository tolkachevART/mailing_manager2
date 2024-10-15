from django.contrib import admin

from mailing.models import Client, Message, Mailing, Logs


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'commentary',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('topic',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'interval', 'status', 'is_activated',)


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'last_datetime_sending', 'status',)
