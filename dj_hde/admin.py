from django.contrib import admin

from .models import Config, Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ('domain', 'email', 'is_active')
