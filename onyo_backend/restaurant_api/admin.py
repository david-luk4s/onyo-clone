from django.contrib import admin
from restaurant_api.models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'phone', 'name_restaurant', 'message', 'date_register')

    def first_name(self, obj):
        return obj.name.split(' ')[0]