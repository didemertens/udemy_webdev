from django import template

register = template.Library()

@register.filter(name='my_cut')
def my_cut(value,arg):
  """
  this cuts out all values of 'arg' from the string
  """
  return value.replace(arg,'')

# register.filter('my_cut',my_cut)
# can also use decorators, @register.filter...
