from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from django.shortcuts import render, get_object_or_404
from book_app.models import Blog

# Create your views here.
class IndexView(TemplateView):
  template_name = 'book_app/index.html'


# class BlogView(ListView):
#   model = Blog

#   def get_blog_posts(self):
#     return Blog.objects.filter(by_date)

class BlogListView(ListView):
    model = Blog

class BlogDetailView(DetailView):
    model = Blog

# def blog_view(request):
#   blogs = Blog.objects.all()
#   context = {
#   'title': 'Latest Posts',
#   'blogs' : blogs
#   }
#   return render(request, 'book_app/view_blogs.html',context)

# def detail_blogs(request,pk):
#   blog = get_object_or_404(Blog, pk=pk)
#   return render(Blog.objects.get(pk=pk))
