from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()


class suppliers(models.Model):
    name = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class philG(models.Model):
    reference = models.CharField(max_length=20)
    project = models.TextField()
    supplier = models.ManyToManyField(suppliers)
    invitation = models.FileField(blank=True, null=True)
    notice_of_award = models.FileField(blank=True, null=True)
    approve_contract = models.FileField(blank=True, null=True)
    notice_to_proceed = models.FileField(blank=True, null=True)
    remarks = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.reference

