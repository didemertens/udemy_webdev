from django.db import models

# Create your models here.
class Blog(models.Model):
  title = models.CharField(max_length=200, unique=True)
  slug = models.SlugField(max_length=100, unique=True)
  body = models.TextField()
  posted = models.DateField(db_index=True, auto_now_add=True)

  def __str__(self):
    return self.title

  # def get_absolute_url(self):
  #   return ('view_blogs',None, { 'slug': self.slug })
