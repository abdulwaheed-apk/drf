from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=250, blank=False)
    body = models.TextField()
    completed= models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']