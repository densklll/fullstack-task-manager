import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks() 
# 2023-01-17: Describe swagger path in local README (local dev)

# 2023-01-30: Describe DRF pagination cursor vs offset (CI runner)
