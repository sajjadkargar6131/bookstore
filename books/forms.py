from django import forms

from .models import Book, Comment

class BookCreateForm(forms.ModelForm):
    class Meta :
        model = Book
        fields = ('title', 'description', 'author', 'price', 'cover', )
        labels = {
            'title' : 'عنوان',
            'description' : 'توضیحات',
            'author' : 'نویسنده',
            'price' : 'قیمت',
            'cover' : 'عکس جلد',
        }

class CommentForm(forms.ModelForm):
    class Meta :
        model = Comment
        fields = ('text', 'recomended', )
        labels = {
            'text' : 'نظر شما ',
            'recomended' : 'توصیه به خرید میکنم'
        }