from django.contrib import admin
from .models import CreateModel, TicketModel


@admin.register(CreateModel)
class CreateAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


@admin.register(TicketModel)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


