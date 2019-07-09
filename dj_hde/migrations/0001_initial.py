# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-09 17:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='APICredentials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=128, verbose_name='Домен')),
                ('email', models.EmailField(max_length=254, verbose_name='Эл. почта')),
                ('api_key', models.CharField(max_length=256, verbose_name='API ключ')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активны')),
            ],
            options={
                'verbose_name_plural': 'Учетные данные',
                'verbose_name': 'Учетные данные',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('data', django_mysql.models.JSONField(default=dict, max_length=256, verbose_name='Данные заявки')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name_plural': 'Заявки',
                'verbose_name': 'Заявка',
            },
        ),
    ]
