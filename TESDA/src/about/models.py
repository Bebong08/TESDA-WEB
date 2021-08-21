from django.db import models

class About (models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title