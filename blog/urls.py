from django.urls import path
from . import views
from .views import Post_ListView, Post_DetailView

urlpatterns = [
    path('', Post_ListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', Post_DetailView.as_view(), name='post-detail'), # pk as primary key
    path('about/', views.about, name='blog-about'),
]