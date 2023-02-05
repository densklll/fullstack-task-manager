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
