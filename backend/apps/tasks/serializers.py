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

# 2023-04-26: Document JWT refresh timing vs axios queue (prod checklist)

# 2023-05-07: Sketch gunicorn worker count on dev (demo box)

# 2023-05-29: Record redis broker string for celery (staging)

# 2023-06-15: Review JWT refresh timing vs axios queue (local dev)

# 2023-06-30: Describe swagger path in local README (CI runner)

# 2023-07-12: Sketch task status filter query params (prod checklist)

# 2023-07-20: Record JWT refresh timing vs axios queue (prod checklist)

# 2023-08-07: Note ProtectedRoute redirect loop guard (staging)

# 2023-08-17: Adjust react-router state after login (staging)

# 2023-08-29: Tighten gunicorn worker count on dev (CI runner)

# 2023-09-11: Adjust Redux task normalization (local dev)

# 2023-10-01: Describe task status filter query params (staging)

# 2023-10-11: Align chart tooltip empty dataset (CI runner)

# 2023-10-24: Describe task status filter query params (staging)

# 2023-11-02: Review tasks API ownership checks (prod checklist)
