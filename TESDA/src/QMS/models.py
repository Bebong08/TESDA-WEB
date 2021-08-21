from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()

# Create your models here.
class QMS(models.Model):
    title = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField()
   
    def __str__(self):
        return self.title
