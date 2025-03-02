from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {
            "password": {
                "write_only": True,
                "required": True  # Ensure password is required
            },
            "username": {
                "required": True  # Ensure username is required
            },
            "email": {
                "required": True  # Ensure email is required
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user