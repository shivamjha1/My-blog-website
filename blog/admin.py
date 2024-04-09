from django.contrib import admin

# Register your models here.
from .models import Blog,Author,Tags

admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Tags)