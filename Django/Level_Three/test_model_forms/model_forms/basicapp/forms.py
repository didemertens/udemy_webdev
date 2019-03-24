from django import forms
from basicapp.models import User
from django.core.exceptions import ValidationError

class NewUserForm(forms.ModelForm):
  # message = forms.CharField(max_length=1000, widget=forms.Textarea,label='Write a message')
  # verify_email = forms.EmailField(label='Enter your email again')

  def clean(self):
    all_clean_data = super(NewUserForm, self).clean()
    if all_clean_data['email'] != all_clean_data['verify_email']:
      raise forms.ValidationError("Make sure emails match")
    return all_clean_data

  class Meta:
    model = User
    fields = ['name','email','verify_email']



