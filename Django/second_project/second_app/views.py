from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  my_dict = {'help_me': "Hello there, what can I help you with?"}
  return render(request, 'second_app/index.html',context=my_dict)

