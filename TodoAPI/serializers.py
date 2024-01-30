
from rest_framework import serializers
from django.contrib.auth.models import User  
from .models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  

    class Meta:
        model = ToDo
        fields = ['id', 'user', 'todoname', 'description', 'completed', 'date_created']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user  
        return ToDo.objects.create(**validated_data)