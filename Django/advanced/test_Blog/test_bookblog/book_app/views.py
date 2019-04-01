from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.shortcuts import render_to_response, get_object_or_404
from book_app.models import Blog

# Create your views here.
class IndexView(TemplateView):
  template_name = 'book_app/index.html'


def BlogView(ListView):
  model = Blog

  def get_blog_posts(self):
    return Blog.objects.filter(by_date)
