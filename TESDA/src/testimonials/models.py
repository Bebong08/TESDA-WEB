from django.db import models

# Create your models here.
class testimonials(models.Model):
    name = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    vids =  models.FileField(upload_to='videos/')
    def __str__(self):
        return self.name