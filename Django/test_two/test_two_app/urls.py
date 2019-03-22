from django.urls import path
from test_two_app import views

urlpatterns = [
    path('', views.index, name="index")
]
