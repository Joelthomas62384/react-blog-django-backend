from rest_framework import serializers
from . models import *





class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields=["id",'username', 'password', 'email', 'phone_number', 'address']
        read_only_fields = ['id']


    def create(self, validated_data):
        # Override the create method to set the password securely
        password = validated_data.pop('password', None)
        user = UserProfile(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user