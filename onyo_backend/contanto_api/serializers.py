from rest_framework import serializers
from contanto_api.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'assunto', 'message']