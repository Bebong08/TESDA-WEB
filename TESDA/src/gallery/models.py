from django.db import models

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    picture = models.ImageField()
    timestamp = models.DateTimeField(auto_now_add=True)
    slider = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class Vids(models.Model):
    title = models.CharField(max_length = 100)
    video =  models.FileField(upload_to='videos/')
    timestamp = models.DateTimeField(auto_now_add=True)
    slider = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class Seals(models.Model):
    title = models.CharField(max_length = 100)
    picture = models.ImageField()
    def __str__(self):
        return self.title