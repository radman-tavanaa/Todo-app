from django.db import models
from datetime import date

# Create your models here.
class TodoModel(models.Model):
    name = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now=False, auto_now_add=False , null=True)
    
    def __str__(self):
        return self.name
    