from django.urls import path,include
from . import views

app_name='book_app'

urlpatterns = [
  path('',views.IndexView.as_view(),name='index'),
  path('blogs/',views.blog_view,name='blogs'),
  # path('blogs/',views.BlogView.as_view(),name='blogs'),
]
