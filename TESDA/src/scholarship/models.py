from django.db import models

# Create your models here.
class Scholarship(models.Model):
    type = models.CharField(max_length = 100)
    picture = models.ImageField()
    
    def __str__(self):
        return self.type