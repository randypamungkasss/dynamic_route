from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextFieldField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)