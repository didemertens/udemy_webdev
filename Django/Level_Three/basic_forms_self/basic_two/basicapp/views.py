from django.shortcuts import render
from django.http import HttpResponseRedirect
from basicapp import forms

# Create your views here.
def index(request):
  return render(request,'basicapp/index.html')

def form_page(request):
  form = forms.NameForm()
  if request.method == 'POST':
    form = forms.NameForm(request.POST)

  if form.is_valid():
    # return HttpResponse('Thanks '+ form.cleaned_data['name'] + '!')
    return HttpResponseRedirect('/form/thanks/')
  else:
    form = forms.NameForm()
  return render(request,'basicapp/nameform.html',{'form':form})

def thanks(request):
  return render(request, 'basicapp/thanks.html')
