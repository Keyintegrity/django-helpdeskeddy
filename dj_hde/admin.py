from django.contrib import admin

from .models import APICredentials, Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)


@admin.register(APICredentials)
class APICredentialsAdmin(admin.ModelAdmin):
    pass
