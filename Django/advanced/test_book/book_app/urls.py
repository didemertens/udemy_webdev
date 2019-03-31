from django.urls import path
from . import views

app_name = 'book_app'

urlpatterns = [
  path('',views.IndexView.as_view(), name='index'),
  path('authors/',views.AuthorListView.as_view(),name='list'),
  path('authors/<int:pk>/',views.AuthorDetailView.as_view(),name='detail'),
]
