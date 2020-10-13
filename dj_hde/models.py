from django.conf import settings
from django.db import models
from django_mysql.models import JSONField
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.utils.translation import gettext_lazy as _


class Department(models.Model):
    name = models.CharField(_('Наименование'), max_length=128)
    department_id = models.PositiveSmallIntegerField(
        verbose_name=_('id департамента'),
        help_text=_('Для добавленяи в запросы создания заявок, пользователя и т.д.'),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('Департамент')
        verbose_name_plural = _('Департаменты')

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)


class Config(models.Model):
    domain = models.CharField(max_length=128, verbose_name=_('Домен'))
    email = models.EmailField(verbose_name=_('Эл. почта'))
    api_key = models.CharField(max_length=256, verbose_name=_('API ключ'))
    departments = models.ManyToManyField(Department, verbose_name=_('Департаменты'))
    is_active = models.BooleanField(default=False, verbose_name=_('Активны'))
    site = models.ForeignKey(Site, default=1, on_delete=models.CASCADE, verbose_name=_('ID Сайта'))

    objects = models.Manager()
    on_site = CurrentSiteManager()

    class Meta:
        verbose_name = _('Настройки')
        verbose_name_plural = _('Настройки')


class Ticket(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата и время создания'))
    data = JSONField(max_length=256, verbose_name=_('Данные заявки'))
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('Пользователь'),
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _('Заявка')
        verbose_name_plural = _('Заявки')
