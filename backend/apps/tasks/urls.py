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
