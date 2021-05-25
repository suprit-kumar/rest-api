from rest_framework import serializers
from api_app import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        # fields = ['user_id', 'name', 'city', 'state', 'about', 'status']
        # exclude = ['user_created_time']
        fields = '__all__'

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
