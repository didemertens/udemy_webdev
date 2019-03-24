from django.db import models
from django.core import validators
from .validators import validate_blacklist


# Create your models here.

class User(models.Model):
  name = models.CharField(max_length=100,validators=[validate_blacklist])
  email = models.EmailField(max_length=100)
  verify_email = models.EmailField(max_length=100)
  # message = models.CharField(max_length=1000)

  def __str__(self):
    return self.name + ' : ' + self.email
