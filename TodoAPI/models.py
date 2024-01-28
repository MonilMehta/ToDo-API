from django.db import models

# Create your models here.
class ToDo(models.Model):
    todoname=models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)