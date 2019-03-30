from django.db import models
from django.urls import reverse

# Create your models here.

class Author(models.Model):
  name = models.CharField(max_length=200)
  birthplace = models.CharField(max_length=200)
  born = models.PositiveIntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("book_app:detail",kwargs={'pk':self.pk})


class Book(models.Model):
  title = models.CharField(max_length=200)
  published = models.PositiveIntegerField()
  author = models.ForeignKey(Author,related_name="books",on_delete=models.CASCADE)

  def __str__(self):
    return self.title
