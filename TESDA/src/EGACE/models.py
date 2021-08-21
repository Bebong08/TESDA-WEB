from django.db import models

# Create your models here.
class egace(models.Model):
    months = models.CharField(max_length = 100)
    enrolled = models.IntegerField()
    perc_enrolled = models.DecimalField(max_digits=5, decimal_places=2)
    graduate = models.IntegerField()
    perc_graduate = models.DecimalField(max_digits=5, decimal_places=2)
    assessed = models.IntegerField()
    perc_assessed = models.DecimalField(max_digits=5, decimal_places=2)
    certified =models.IntegerField()
    perc_certified = models.DecimalField(max_digits=5, decimal_places=2)
    employed = models.IntegerField()
    perc_employed = models.DecimalField(max_digits=5, decimal_places=2)
    date_entry = models.DateTimeField(auto_now_add=True)
    # picture = models.ImageField()
 
    def __str__(self):
        return self.months