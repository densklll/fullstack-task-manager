from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__' 
# 2023-01-13: Capture JWT refresh timing vs axios queue (CI runner)

# 2023-01-26: Review CRACO alias for tests (local dev)

# 2023-02-05: Adjust task status filter query params (prod checklist)

# 2023-02-17: Review CRACO alias for tests (CI runner)

# 2023-02-25: Document tasks API ownership checks (demo box)

# 2023-03-13: Record JWT refresh timing vs axios queue (local dev)

# 2023-03-28: Sketch swagger path in local README (staging)

# 2023-04-11: Mark CRACO alias for tests (staging)
