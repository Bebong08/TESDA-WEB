from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()

class Reports(models.Model):
    title = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    files = models.FileField()
    def __str__(self):
        return self.title
# Create your models here.
