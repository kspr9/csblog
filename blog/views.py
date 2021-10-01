from django.shortcuts import render
# checks that user is logged in before posting or updating when using view class
# (was done with a @decorator when using view method)
# UserPassesTestMixin allows only the author of the post to edit posts, prevents other users editing other users posts
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#importing Post model to be used for class based views // or earlier in home function
from .models import Post
#importing list views for class based views
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
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

# acts as Home at the moment
class Post_ListView(ListView):
    model = Post # 'Post' defined in models.py
    template_name = 'blog/home.html' # << change here to customize << default url is <app>/<model>_<viewtype>.html  (eg'blog/post_list') 
    context_object_name = 'posts' # home.html loops over 'for post in posts', this line here gives current context object (ie model = Post) a name  = current model ie Post model
    ordering = ['-date_posted'] # orders posts from newest to oldest
    paginate_by = 5

class Post_DetailView(DetailView):
    model = Post # 'Post' defined in models.py
    # don't forget to add to urlpatterns
    # looking for a template 
    # 'blog/post_detail'

class Post_CreateView(LoginRequiredMixin, CreateView):
    model = Post # 'Post' defined in models.py
    fields = ['title', 'content']

    # Since blog_post requires an author, then only above lines provide only form fields, but do not define the author for the post.
    # below we define that post has author and that author is the current logged in user.
    # overrride form_valid method > ie tell the program that post has an author while creating
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # looking for a template 
    # 'blog/post_create'

class Post_UpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post # 'Post' defined in models.py
    fields = ['title', 'content']

    # override form_valid method > ie tell the program that post has an author while creating
    def form_valid(self, form):
        form.instance.author = self.request.user # sets user of the request as author of the form
        return super().form_valid(form)

    # checks that only the author of the post is able to edit the post
    def test_func(self):
        post = self.get_object() # selects the current post
        if self.request.user == post.author:
            return True
        return False

    # looking for a template 
    # 'blog/post_create'

class Post_DeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post # 'Post' defined in models.py
    success_url = '/'

    # checks that only the author of the post is able to edit the post
    def test_func(self):
        post = self.get_object() # selects the current post
        if self.request.user == post.author:
            return True
        return False

    # don't forget to add to urlpatterns
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