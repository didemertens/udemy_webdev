from django import forms
from django.core import validators

# because of value, django knows it's a validator
def check_for_z(value):
  if value[0].lower() != 'z':
    raise forms.ValidationError("Needs to start with z")

class FormName(forms.Form):
  name = forms.CharField(validators=[check_for_z])
  email = forms.EmailField()
  verify_email = forms.EmailField(label='Enter your email again')
  text = forms.CharField(widget=forms.Textarea)
  botcatcher = forms.CharField(required=False,
                              widget=forms.HiddenInput,
                              validators=[validators.MaxLengthValidator(0)])

  # def clean_botcatcher(self):
  #   botcatcher = self.cleaned_data['botcatcher']
  #   if len(botcatcher) > 0:
  #     raise forms.ValidationError("Gotcha")
  #   return botcatcher

  def clean(self):
    # grab all data of form and clean, check data
    all_clean_data = super().clean()
    email = all_clean_data['email']
    vmail = all_clean_data['verify_email']
    if email != vmail:
      raise forms.ValidationError("Make sure emails match")
