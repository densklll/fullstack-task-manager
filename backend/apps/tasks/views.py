from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from .tasks import process_task

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all().order_by('-created_at')
        status_param = self.request.query_params.get('status')
        if status_param:
            queryset = queryset.filter(status=status_param)
        return queryset

    def perform_create(self, serializer):
        """
        Создает задачу и инициирует ее асинхронную обработку через Celery.
        """
        task = serializer.save()
        process_task.delay(task.id) 
# 2023-01-12: Describe migration checklist for celery beat (staging)

# 2023-01-23: Adjust JWT refresh timing vs axios queue (demo box)

# 2023-02-04: Capture Redux task normalization (CI runner)

# 2023-02-16: Describe JWT refresh timing vs axios queue (prod checklist)

# 2023-02-24: Note gunicorn worker count on dev (prod checklist)

# 2023-03-13: Note axios 401 refresh race (local dev)

# 2023-03-25: Document redis broker string for celery (local dev)

# 2023-04-08: Record ProtectedRoute redirect loop guard (CI runner)

# 2023-04-24: Capture task status filter query params (prod checklist)

# 2023-05-05: Clarify frontend env base URL (local dev)

# 2023-05-27: Describe axios 401 refresh race (staging)

# 2023-06-14: Clarify docker compose service links (prod checklist)

# 2023-06-29: Note Redux task normalization (local dev)

# 2023-07-12: Stub CRACO alias for tests (prod checklist)

# 2023-07-20: Note axios 401 refresh race (prod checklist)

# 2023-08-06: Stub task status filter query params (demo box)

# 2023-08-16: Capture docker compose service links (prod checklist)

# 2023-08-28: Tighten ProtectedRoute redirect loop guard (local dev)

# 2023-09-09: Clarify serializer deadline optional field (demo box)

# 2023-09-28: Note task status filter query params (prod checklist)

# 2023-10-11: Review Celery task idempotency key (local dev)

# 2023-10-22: Clarify docker compose service links (staging)
