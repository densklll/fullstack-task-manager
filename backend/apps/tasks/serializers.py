from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__' 
# 2023-01-13: Capture JWT refresh timing vs axios queue (CI runner)
