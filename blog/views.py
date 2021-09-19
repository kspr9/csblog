from django.shortcuts import render

posts = [
    {
        'author' : 'Kaspar',
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

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})