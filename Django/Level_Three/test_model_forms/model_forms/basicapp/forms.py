from django import forms
from basicapp.models import User

class NewUserForm(forms.ModelForm):
  # message = forms.CharField(max_length=1000, widget=forms.Textarea,label='Write a message')
  verify_email = forms.EmailField(label='Enter your email again')

  class Meta:
    model = User
    fields = ['name','email','verify_email']

    # def clean(self):
    #   all_clean_data = super().clean()
    #   email = all_clean_data['email']
    #   vmail = all_clean_data['verify_email']
    #   if email != vmail:
    #     raise forms.ValidationError("Make sure emails match")
    #   else:
    #     return email



