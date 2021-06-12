from rest_framework import serializers
from api_app import models
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['user_id', 'name', 'city', 'state', 'about', 'status']
        # exclude = ['user_created_time']

    def validate(self, data):

        if len(data['name']) < 3:
            raise serializers.ValidationError({'error': 'Name must have minimum 3 characters'})

        # for i in range(10):
        #     if str(i) in data['name']:
        #         raise serializers.ValidationError({'error': "Name can't contain any digits"})

        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({'error': "Name can't be alphanumeric"})

        return data




class UsrSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


    def create(self, validated_data): # Overwrite method and create hash password for user
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['category_name']


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Foreign Key

    class Meta:
        model = models.Book
        fields = ['category', 'boot_title']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'

    def validate(self, data):

        if len(data['name']) < 3:
            raise serializers.ValidationError({'error': 'Name must have minimum 3 characters'})

        if data['age'] < 18:
            raise serializers.ValidationError({'error': 'Age must be greater than 18'})

        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({'error': "Name can't be alphanumeric"})

        return data
