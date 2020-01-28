from django.contrib import admin
from contanto_api.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'assunto', 'message', 'date_register')
