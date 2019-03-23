from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import User

# Create your views here.
def index(request):
  my_dict = {'help_me': "Hello there, what can I help you with?"}
  return render(request, 'second_app/index.html',context=my_dict)

def user(request):
  user_list = User.objects.order_by('first_name')
  user_dict = {'user_data' : user_list}
  return render(request,'second_app/user.html',context=user_dict)
