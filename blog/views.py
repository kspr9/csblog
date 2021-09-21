from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all() # was posts referring to static posts list variable above
    }
    return render(request, 'blog/home.html', context)

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