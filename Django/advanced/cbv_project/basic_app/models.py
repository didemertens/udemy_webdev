from django.db import models

# Create your models here.
class School(models.Model):
  name = models.CharField(max_length=256)
  principal = models.CharField(max_length=256)
  location = models.CharField(max_length=256)

  def __str__(self):
    return self.name

class Student(models.Model):
  name = models.CharField(max_length=256)
  age = models.PositiveIntegerField()
  school = models.ForeignKey(School,related_name='students',on_delete=models.PROTECT)

# foreign key because you want to use the School class

  def __str__(self):
    return self.name
