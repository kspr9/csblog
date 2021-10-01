from django.urls import path
from . import views
from .views import (
    Post_ListView, 
    Post_DetailView,
    Post_CreateView,
    Post_UpdateView,
    Post_DeleteView,
    User_Post_ListView
)

urlpatterns = [
    path('', Post_ListView.as_view(), name='blog-home'),
    path('user/<str:username>/', User_Post_ListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', Post_DetailView.as_view(), name='post-detail'), # pk as primary key
    path('post/new/', Post_CreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', Post_UpdateView.as_view(), name='post-update'), # pk as primary key
    path('post/<int:pk>/delete/', Post_DeleteView.as_view(), name='post-delete'), # pk as primary key
    path('about/', views.about, name='blog-about'),
]