from django.views.generic import TemplateView,ListView,DetailView,CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from book_app.models import Blog,Comment
from .forms import PostForm, CommentForm

# Create your views here.
class IndexView(TemplateView):
  template_name = 'book_app/index.html'

class BlogListView(ListView):
  model = Blog

class BlogDetailView(DetailView):
  model = Blog

class CreatePostView(LoginRequiredMixin,CreateView):
  login_url = '/login/'
  redirected_field_name='book_app/blog_detail.html'
  form_class = PostForm
  model = Blog


def add_comment_to_post(request, pk):
  blog = get_object_or_404(Blog, pk=pk)
  if request.method == "POST":
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.blog = blog
        comment.save()
        return redirect('book_app:blog_detail', pk=blog.pk)
  else:
    form = CommentForm()
  return render(request, 'book_app/add_comment_to_post.html', {'form': form})
