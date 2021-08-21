from django.db import models

# Create your models here.
class Center(models.Model):
    center = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.center

class Classification(models.Model):
    centertype = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.centertype
    
class Qualifications(models.Model):
    description = models.TextField()
    trainingcenter =  models.ManyToManyField(Center)
    centerclass =  models.ManyToManyField(Classification)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.description