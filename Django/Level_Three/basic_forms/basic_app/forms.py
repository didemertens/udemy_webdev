from django import forms
from django.core import validators

# because of value, django knows it's a validator
def check_for_z(value):
  if value[0].lower() != 'z':
    raise forms.ValidationError("Needs to start with z")

class FormName(forms.Form):
  name = forms.CharField(validators=[check_for_z])
  email = forms.EmailField()
  text = forms.CharField(widget=forms.Textarea)
  botcatcher = forms.CharField(required=False,
                              widget=forms.HiddenInput,
                              validators=[validators.MaxLengthValidator(0)])

  # def clean_botcatcher(self):
  #   botcatcher = self.cleaned_data['botcatcher']
  #   if len(botcatcher) > 0:
  #     raise forms.ValidationError("Gotcha")
  #   return botcatcher


