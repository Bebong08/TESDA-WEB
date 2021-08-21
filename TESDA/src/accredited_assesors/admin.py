from django.contrib import admin

# Register your models here.
from .models import  accredited_assesors,Gender,Center,Qualifications

admin.site.register(Gender)
admin.site.register(accredited_assesors)
admin.site.register(Center)
admin.site.register(Qualifications)
