from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView
from . import models, forms
from django.shortcuts import get_object_or_404
# Create your views here.
class BookListView(ListView):
    template_name = 'books/book_list.html'
    queryset = models.Books.objects.all()

    def get_queryset(self):
        return models.Books.objects.all()

class BookCreateView(CreateView):
        template_name = 'books/book_create.html'
        form_class = forms.BookForms
        success_url = '/'
        queryset = models.Books.objects.all()

        def form_valid(self, form):
            return super().form_valid(form=form)

class BookDetailView(DetailView):
    template_name = 'book/book_detail.html'


    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=id_)