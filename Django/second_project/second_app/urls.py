from second_app import views
from django.urls import path

urlpatterns = [
  path('users/',views.user,name='user'),
  path('',views.index,name='index'),
]

