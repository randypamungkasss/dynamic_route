from django.db import models
from core.models import BaseModel

# Create your models here.
class Todo(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextFieldField(blank=True, null=True)

