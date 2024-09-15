from rest_framework import serializers
from tasks.models import Task
from django.contrib.auth import get_user_model
User = get_user_model()

# Task Serializer also filters tasks by user using a foreign key relationship.
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user'] 

# User Serializer also includes basic validation for user data
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
