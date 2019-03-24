from django.shortcuts import render
from basicapp.forms import NewUserForm
from django.contrib import messages

# Create your views here.
def index(request):
  return render(request, 'basicapp/index.html')

def user(request):

  form = NewUserForm()

  if request.method == 'POST':
    form = NewUserForm(request.POST)

    if form.is_valid():
      form.save(commit="True")
      messages.success(request, 'The form is submitted.')
    else:
      messages.error(request, 'The form is invalid. Try again.')

  return render(request, 'basicapp/user.html', {'form': form})
