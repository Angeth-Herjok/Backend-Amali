from rest_framework import serializers
from sponsors.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'phoneNumber', 'organisation', 'bio')
