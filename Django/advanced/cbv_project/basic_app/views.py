from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models

# from django.http import HttpResponse

# # Create your views here.
# def index(request):
#   return render(request,'index.html')

# class CBView(View):

#   def get(self,request):
#     return HttpResponse('Class based views are cool!')

class IndexView(TemplateView):
  template_name = 'index.html'

  def get_context_data(self,**kwargs):
    # kwargs gives a dictionary, args is for undefinied amount of arguments
    context = super().get_context_data(**kwargs)
    context['injectme'] = 'Basic injection!'
    return context

class SchoolListView(ListView):
  context_object_name = 'schools'
  model = models.School

  # returns a list with the name school_list, if you want to define your own name add contect_object_name

class SchoolDetailView(DetailView):
  context_object_name = 'school_details'
  model = models.School
  template_name = 'basic_app/school_detail.html'

# returns the model in lower case, not with _detail
