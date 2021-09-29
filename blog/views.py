from django.shortcuts import render
from .models import Post
#importing list views for class based views
from django.views.generic import ListView, DetailView


# Here defining all the views that are then configured to be shown in urls.py in urlpatterns

# view used before adding class Post_ListView, was used in urlpatterns.py "path('', views.home, name='blog-home'),
#def home(request):
#    context = {
#        'posts': Post.objects.all() # was posts referring to static posts list variable commented out below, now dynamic getting all Post's objects
#    }
#    return render(request, 'blog/home.html', context)

class Post_ListView(ListView):
    model = Post # 'Post' defined in models.py
    template_name = 'blog/home.html' # default url is <app>/<model>_<viewtype>.html << change here to custom
    context_object_name = 'posts' # home.html loops over 'for post in posts', this line here gives current context object (ie model = Post) a name  = current model ie Post model
    ordering = ['-date_posted'] # orders posts from newest to oldest

class Post_DetailView(DetailView):
    model = Post # 'Post' defined in models.py

    # looking for a template 
    # 'blog/post_detail'

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

'''
Previous dummy data
posts = [
    {
        'author': 'Kaspar',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'September 19, 2021'
    },
    {
        'author': 'Liisi',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'September 29, 2021'
    }
]
'''