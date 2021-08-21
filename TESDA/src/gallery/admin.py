from django.contrib import admin

# Register your models here.
from .models import Gallery,Vids,Seals

admin.site.register(Gallery)
admin.site.register(Vids)
admin.site.register(Seals)