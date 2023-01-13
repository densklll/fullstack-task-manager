from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'', TaskViewSet, basename='task')

urlpatterns = router.urls 
# 2023-01-13: Document JWT refresh timing vs axios queue (CI runner)
