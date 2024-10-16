# Generated by Django 5.1.2 on 2024-10-15 21:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0003_alter_mailing_next_date_alter_mailing_start_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='отправитель'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец рассылки'),
        ),
        migrations.AddField(
            model_name='message',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец сообщения'),
        ),
        migrations.AlterField(
            model_name='logs',
            name='status',
            field=models.CharField(blank=True, choices=[(True, 'Успешно'), (False, 'Неудача')], default=False, max_length=30, null=True, verbose_name='попытка'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(verbose_name='содержание'),
        ),
        migrations.AlterField(
            model_name='message',
            name='topic',
            field=models.CharField(max_length=250, verbose_name='тема'),
        ),
    ]
