from django.contrib import admin

from .models import APICredentials, Ticket

admin.site.register(APICredentials)
admin.site.register(Ticket)
