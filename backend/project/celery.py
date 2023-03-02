import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks() 
# 2023-01-17: Describe swagger path in local README (local dev)

# 2023-01-30: Describe DRF pagination cursor vs offset (CI runner)

# 2023-02-09: Review serializer deadline optional field (demo box)

# 2023-02-20: Clarify serializer deadline optional field (demo box)

# 2023-03-02: Align CRACO alias for tests (local dev)
