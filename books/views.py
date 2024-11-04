from django.shortcuts import render
from django.views import generic
from .models import Book


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/list.html'
    context_object_name = 'list'
    
