from django.shortcuts import render
from django.views.generic.edit import FormMixin
from django.views import generic
from django.urls import reverse

from .models import Book
from .forms import BookCreateForm, CommentForm

class BookListView(generic.ListView):
    model = Book
    paginate_by = 8
    template_name = 'books/book_list.html'
    context_object_name = 'books'
  
    
class BookDetailView(generic.DetailView, FormMixin):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    form_class =  CommentForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['form'] = self.get_form()
        return context
    
    def get_success_url(self):
        return reverse('book_detail', kwargs={'pk' : self.object.pk})
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment  = form.save(commit=False)
            comment.book = self.object
            comment.user = request.user
            comment.save()
            return self.form_valid(form)
        else :
            return self.form_invalid(form)
            
            
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
