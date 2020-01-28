from rest_framework import viewsets
from restaurant_api.serializers import RestaurantSerializer
from restaurant_api.models import Restaurant

from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class RestaurantViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
