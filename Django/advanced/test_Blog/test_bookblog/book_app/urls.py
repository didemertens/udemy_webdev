from django.urls import path,include
from . import views

app_name='book_app'

urlpatterns = [
  path('',views.IndexView.as_view(),name='index'),
  path('blog/',views.BlogListView.as_view(),name='blog_list'),
  path('blog/<int:pk>',views.BlogDetailView.as_view(),name='blog_detail'),
  # path('blog/<int:pk>/comment/', views.add_comment_to_post,name='add_comment_to_post'),
]

  # path('blogs/',views.BlogView.as_view(),name='blog_list'),
