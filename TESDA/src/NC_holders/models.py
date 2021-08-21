from django.db import models

# Create your models here.
class NCHolders(models.Model):
    lastname = models.CharField(max_length = 100)
    firstname = models.CharField(max_length = 100)
    middlename = models.CharField(max_length = 100)
    extname = models.CharField(max_length = 100)
    certType = models.CharField(max_length = 100)
    NCTitle = models.TextField()
    COCTitle = models.TextField()
    date_released = models.DateField()
    expiration_date = models.DateField()
    # picture = models.ImageField()
    list_filter = (('',))
    def __str__(self):
        return self.lastname + ', ' + self.firstname