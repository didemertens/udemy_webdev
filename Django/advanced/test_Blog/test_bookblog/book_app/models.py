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

# class Comment(models.Model):
#   blog = models.ForeignKey('book_app.Blog',related_name='comments',on_delete=models.CASCADE)
#   author = models.CharField(max_length=200,null=True)
#   text = models.TextField(null=True)

#   def __str__(self):
#     return self.text
