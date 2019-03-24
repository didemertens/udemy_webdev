from django.db import models
from django.core import validators


# Create your models here.

class User(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  verify_email = models.EmailField(max_length=100)
  # message = models.CharField(max_length=1000)

  def __str__(self):
    return self.name + ' : ' + self.email

  # def clean(self):
  #   all_clean_data = super().clean()
  #   email = all_clean_data['email']
  #   vmail = all_clean_data['verify_email']
  #   if email != vmail:
  #     raise forms.ValidationError("Make sure emails match")
  #   else:
  #     return all_clean_data
