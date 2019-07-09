from django.conf import settings
from django.db import models
from django_mysql.models import JSONField


class APICredentials(models.Model):
    domain = models.CharField(max_length=128, verbose_name='Домен')
    email = models.EmailField(verbose_name='Эл. почта')
    api_key = models.CharField(max_length=256, verbose_name='API ключ')
    is_active = models.BooleanField(default=False, verbose_name='Активны')

    class Meta:
        verbose_name = 'Учетные данные'
        verbose_name_plural = 'Учетные данные'


class Ticket(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    data = JSONField(max_length=256, verbose_name='Данные заявки')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', null=True, blank=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
