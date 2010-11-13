from django.contrib import admin

from models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published')
    prepopulated_fields = {"slug": ("title",)}
    pass
    
admin.site.register(Post, PostAdmin)