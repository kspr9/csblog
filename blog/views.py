from django.shortcuts import render
#importing Post model to be used for class based views // or earlier in home function
from .models import Post
#importing list views for class based views
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView
)


# Here defining all the views that are then configured to be shown in urls.py in urlpatterns #
##############################################################################################

# The view used before adding class based views (like Post_ListView), was used in urlpatterns.py "path('', views.home, name='blog-home'),
###################
#def home(request):
#    context = {
#        'posts': Post.objects.all() # was posts referring to static posts list variable commented out below, now dynamic getting all Post's objects
#    }
#    return render(request, 'blog/home.html', context)
##################

class Post_ListView(ListView):
    model = Post # 'Post' defined in models.py
    template_name = 'blog/home.html' # << change here to customize << default url is <app>/<model>_<viewtype>.html  (eg'blog/post_list') 
    context_object_name = 'posts' # home.html loops over 'for post in posts', this line here gives current context object (ie model = Post) a name  = current model ie Post model
    ordering = ['-date_posted'] # orders posts from newest to oldest

class Post_DetailView(DetailView):
    model = Post # 'Post' defined in models.py
    # don't forget to add to urlpatterns
    # looking for a template 
    # 'blog/post_detail'

class Post_CreateView(CreateView):
    model = Post # 'Post' defined in models.py
    fields = ['title', 'content']

    # overrride form_valid method > ie tell the program that post has an author while creating
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # looking for a template 
    # 'blog/post_create'

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