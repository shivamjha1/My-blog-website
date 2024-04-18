from django.contrib import admin

# Register your models here.
from .models import Blog,Author,Tags,Comments

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    
class CommentsAdmin(admin.ModelAdmin):
    list_display=("user_name","blog")

admin.site.register(Blog,BlogAdmin)
admin.site.register(Author)
admin.site.register(Tags)
admin.site.register(Comments,CommentsAdmin)