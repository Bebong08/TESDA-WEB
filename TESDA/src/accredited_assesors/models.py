
from django.db import models

# Create your models here.
class Center(models.Model):
    center = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.center

class Qualifications(models.Model):
    qualification = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.qualification

class Gender(models.Model):
    Sex = models.TextField()
    def __str__(self):
        return self.Sex

class accredited_assesors(models.Model):
    name = models.TextField()
    Institution = models.ManyToManyField(Center)
    Sex = models.ManyToManyField(Gender)
    qualification = models.ManyToManyField(Qualifications)
    def __str__(self):
        return self.name
