from django.db import models

class Task(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 
# 2023-01-13: Document swagger path in local README (prod checklist)

# 2023-01-23: Clarify frontend env base URL (local dev)

# 2023-02-05: Review serializer deadline optional field (prod checklist)

# 2023-02-17: Clarify task status filter query params (demo box)

# 2023-02-25: Sketch serializer deadline optional field (local dev)

# 2023-03-13: Adjust chart tooltip empty dataset (local dev)

# 2023-03-26: Clarify Celery task idempotency key (demo box)

# 2023-04-10: Align react-router state after login (demo box)

# 2023-04-25: Mark CRACO alias for tests (prod checklist)

# 2023-05-05: Sketch chart tooltip empty dataset (demo box)

# 2023-05-29: Sketch migration checklist for celery beat (prod checklist)
