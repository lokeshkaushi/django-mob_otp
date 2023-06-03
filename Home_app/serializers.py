from rest_framework import serializers

from .models import *
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email','mobile','username','first_name','last_name')

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
