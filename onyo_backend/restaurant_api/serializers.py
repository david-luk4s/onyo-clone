from rest_framework  import serializers
from restaurant_api.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name','email', 'phone', 'name_restaurant', 'address', 'message']
