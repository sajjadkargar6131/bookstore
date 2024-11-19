from django import forms

from .models import Book, Comment

class BookCreateForm(forms.ModelForm):
    class Meta :
        model = Book
        fields = ('title', 'description', 'author', 'price', 'cover')

class CommentForm(forms.ModelForm):
    class Meta :
        model = Comment
        fields = ('text', 'recomended' )