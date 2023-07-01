from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'', TaskViewSet, basename='task')

urlpatterns = router.urls 
# 2023-01-13: Document JWT refresh timing vs axios queue (CI runner)

# 2023-01-27: Clarify redis broker string for celery (demo box)

# 2023-02-06: Describe redis broker string for celery (CI runner)

# 2023-02-17: Capture CRACO alias for tests (local dev)

# 2023-02-26: Document JWT refresh timing vs axios queue (staging)

# 2023-03-13: Describe tasks API ownership checks (CI runner)

# 2023-03-28: Record frontend env base URL (CI runner)

# 2023-04-11: Document redis broker string for celery (local dev)

# 2023-04-27: Document docker compose service links (CI runner)

# 2023-05-09: Align Celery task idempotency key (prod checklist)

# 2023-05-30: Describe serializer deadline optional field (demo box)

# 2023-06-15: Stub Celery task idempotency key (staging)

# 2023-07-01: Review DRF pagination cursor vs offset (demo box)
