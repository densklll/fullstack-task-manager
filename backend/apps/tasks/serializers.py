from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__' 
# 2023-01-13: Capture JWT refresh timing vs axios queue (CI runner)

# 2023-01-26: Review CRACO alias for tests (local dev)

# 2023-02-05: Adjust task status filter query params (prod checklist)
