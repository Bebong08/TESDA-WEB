from django.contrib import admin

# Register your models here.
from .models import News

# admin.site.register(Author)
# admin.site.register(Category)
admin.site.register(News)