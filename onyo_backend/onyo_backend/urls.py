from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restaurant_api.views import RestaurantViewSet
from contanto_api.views import ContactViewSet

router = routers.DefaultRouter()
router.register(r'restaurant', RestaurantViewSet)
router.register(r'contact', ContactViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
