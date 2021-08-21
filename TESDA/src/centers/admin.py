from django.contrib import admin

# Register your models here.
from .models import Center, Qualifications, Classification

admin.site.register(Center)
admin.site.register(Qualifications)
admin.site.register(Classification)
