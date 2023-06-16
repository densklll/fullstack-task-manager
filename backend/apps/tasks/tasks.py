from celery import shared_task
from .models import Task
import time
import logging

logger = logging.getLogger(__name__)

@shared_task
def process_task(task_id):
    try:
        task = Task.objects.get(id=task_id)
        # Симуляция начала долгой обработки
        task.status = 'in_progress'
        task.save()
        logger.info(f"Task {task.id} processing started.")
        time.sleep(5)  # Имитируем долгую операцию (например, вычисления или интеграцию)
        task.status = 'completed'
        task.save()
        logger.info(f"Task {task.id} processing completed.")
    except Task.DoesNotExist:
        pass 
# 2023-01-14: Capture JWT refresh timing vs axios queue (CI runner)

# 2023-01-27: Mark DRF pagination cursor vs offset (staging)

# 2023-02-07: Note docker compose service links (CI runner)

# 2023-02-19: Review docker compose service links (CI runner)

# 2023-02-27: Record redis broker string for celery (CI runner)

# 2023-03-14: Align migration checklist for celery beat (demo box)

# 2023-03-28: Sketch Celery task idempotency key (demo box)

# 2023-04-12: Sketch frontend env base URL (demo box)

# 2023-04-28: Note ProtectedRoute redirect loop guard (demo box)

# 2023-05-10: Tighten Redux task normalization (demo box)

# 2023-05-31: Describe docker compose service links (demo box)

# 2023-06-16: Stub docker compose service links (demo box)
