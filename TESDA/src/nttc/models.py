from django.db import models  
from centers.models import Qualifications
# Create your models here.

class NTTC(models.Model):
    name = models.TextField()
    date_released = models.DateField()
    expiration = models.DateField()
    qualification = models.ManyToManyField(Qualifications)
    def __str__(self):
        return self.name


