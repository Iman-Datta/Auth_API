from rest_framework import serializers
from .models import Profile

class RegisterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone', 'age', 'gender']

class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(format="%d %B %Y, %I:%M %p", read_only=True)
    updated_at = serializers.DateTimeField(format="%d %B %Y, %I:%M %p", read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'
