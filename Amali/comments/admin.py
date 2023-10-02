from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'comment', 'likes')
    search_fields = ('full_name', 'comment')
    list_filter = ('likes',)
    