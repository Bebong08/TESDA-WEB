from django.db import models

# Create your models here.
class Stories(models.Model):
    title = models.TextField()
    caption = models.TextField()
    vids =  models.FileField(upload_to='videos/')
    def __str__(self):
        return self.title