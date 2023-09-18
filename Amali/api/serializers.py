from rest_framework import serializers
from sponsors.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'phoneNumber', 'organisation', 'bio')
        extra_kwargs = {'password': {'write_only': True}}









from donation.models import Donation

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'
