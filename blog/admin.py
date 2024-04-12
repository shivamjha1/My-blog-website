from django.contrib import admin

# Register your models here.
from .models import Blog,Author,Tags

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    

admin.site.register(Blog,BlogAdmin)
admin.site.register(Author)
admin.site.register(Tags)