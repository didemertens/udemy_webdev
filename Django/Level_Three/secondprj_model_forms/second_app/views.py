from django.shortcuts import render
# # from django.http import HttpResponse
# from second_app.models import User
from second_app.forms import NewUserForm

# Create your views here.
def index(request):
  my_dict = {'help_me': "Hello there, what can I help you with?"}
  return render(request, 'second_app/index.html',context=my_dict)

def user(request):

  form = NewUserForm()

  if request.method == 'POST':
    form = NewUserForm(request.POST)

    if form.is_valid():
      form.save(commit=True)
      return index(request)
    else:
      print("Error: form invalid")

  return render(request,'second_app/user.html',{'form': form})

