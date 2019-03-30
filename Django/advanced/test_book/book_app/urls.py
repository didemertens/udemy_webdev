from django.urls import path
from . import views

app_name = 'book_app'

urlpatterns = [
  path('',views.AuthorListView.as_view(),name='list'),
  path('<int:pk>/',views.AuthorDetailView.as_view(),name='detail'),
]
