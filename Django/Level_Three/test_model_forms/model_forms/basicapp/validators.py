from django.core.exceptions import ValidationError


blacklist = ['gotcha']

def validate_blacklist(value):
  if value in blacklist:
    raise ValidationError('Sorry, this value is not valid.')
  return value

