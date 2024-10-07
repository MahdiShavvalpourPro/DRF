from rest_framework import serializers
from django.contrib.auth import get_user_model
from todo.models import Todo

user = get_user_model()


class TodoSerializer(serializers.ModelSerializer):

    def validate_priority(self, priority):
        if (priority < 0 or priority > 10):
            raise serializers.ValidationError('priority is not ok ')
        return priority

    def validate(self, attrs):
        print(attrs)
        return super().validate(attrs)

    class Meta:
        model = Todo
        fields = ['id', 'title', 'content', 'priority', 'is_done', 'user']


class UserSerializer(serializers.ModelSerializer):

    todos = TodoSerializer(read_only=True, many=True)

    class Meta:
        model = user
        # fields = ['first_name', 'last_name', 'email']
        fields = '__all__'
