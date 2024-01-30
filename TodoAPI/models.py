from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todoname=models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    email=models.EmailField(unique=True)

    def __str__(self) :
        return  self.user.username