from django.conf.urls import url
from test_app import views
from django.urls import path

urlpatterns = [
  path('',views.index,name='index'),
]
