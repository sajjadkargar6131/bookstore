from django.contrib import admin
from .models import Book, Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'text', 'book', 'datetime_created', 'recomended']
    
    
admin.site.register(Book)

admin.site.register(Comment,CommentAdmin)

