from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from . import models
# Create your views here.

class IndexView(TemplateView):
  template_name = 'index.html'

class AuthorListView(ListView):
  context_object_name = 'authors'
  model = models.Author

class AuthorDetailView(DetailView):
  context_object_name = 'author_detail'
  model = models.Author
  template_name = 'book_app/author_detail.html'
