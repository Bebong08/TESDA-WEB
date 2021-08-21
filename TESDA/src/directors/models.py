from django.db import models

# Create your models here.
class Directors(models.Model):
    name = models.CharField(max_length = 100)
    picture = models.ImageField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name