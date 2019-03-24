from django.core.exceptions import ValidationError


blacklist = ['gotcha']

def validate_blacklist(value):
  if value in blacklist:
    raise ValidationError('Sorry, this value is not valid.')
  return value

# def check_email(value1,value2):
#   if value1 == value2:
#     return value1
#   else:
#     raise ValidationError("Please make sure your emails match.")

