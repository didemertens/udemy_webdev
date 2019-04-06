from django.db import models
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
  title = models.CharField(max_length=200, unique=True)
  body = models.TextField()
  posted = models.DateField(db_index=True, auto_now_add=True)

  def get_absolute_url(self):
    return reverse("book_app:detail_blogs",kwargs={'pk':self.pk})

  def __str__(self):
    return self.title


class Comment(models.Model):
  blog_post = models.ForeignKey('book_app.Blog',on_delete=models.CASCADE,related_name='comments')
  author = models.CharField(max_length=200)
  text = models.TextField()

  def __str__(self):
    return self.text
