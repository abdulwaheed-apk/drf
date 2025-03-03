from rest_framework import serializers
from todos.models import Todo

class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ['id', 'title', 'body', 'completed', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        return Todo.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.save()
        return instance