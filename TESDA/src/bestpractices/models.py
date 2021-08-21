from django.db import models

# Create your models here.
class practices(models.Model):
    title = models.TextField()
    caption = models.TextField()
    pics =  models.ImageField()
    def __str__(self):
        return self.title