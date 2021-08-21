from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.base import Model
from django.urls import reverse
User = get_user_model()
# Create your models here.
# class Author(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)


#     def __str__(self):
#         return self.user.username

# class Category(models.Model):
#     title = models.CharField(max_length=20)

#     def __str__(self):
#         return self.title

class News(models.Model):
    title = models.TextField()
    picture = models.ImageField()
  
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={
            'id': self.id
        })