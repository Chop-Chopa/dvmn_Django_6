from django.contrib import admin
from blog.models import Post, Tag, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at', 'author']
    raw_id_fields = ['author', 'likes', 'tags']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'published_at', 'text', 'post']
    raw_id_fields = ['author', 'post']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
