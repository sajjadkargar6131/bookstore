from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from .models import Book
from .forms import BookCreateForm

class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    
class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    
class BookCreateView(generic.CreateView):
    form_class = BookCreateForm
    template_name = 'books/book_create_update.html'
    extra_context = {'title' : 'Create Book'}
    
class BookUpdateView(generic.UpdateView):
    model =  Book
    form_class = BookCreateForm
    template_name = 'books/book_create_update.html'
    extra_context = {'title' : 'Update Book'}
    
    
class BooKDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    
    def get_success_url(self) -> str:
        return reverse('book_list')
