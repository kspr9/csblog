from django.db import models
# for date_posted
from django.utils import timezone
# importing Users to this
from django.contrib.auth.models import User
# need to find a way to get the url of a blog post created
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # auto_now=True, when need to change time, auto_now_add = when post was created 
    author = models.ForeignKey(User, on_delete=models.CASCADE) # on_delete == when user is deleted, then also post is deleted

    def __str__(self):
        return self.title

    # A method for getting absolute url for a blog post created                #
    # so that user can be routed to that blog posts detail page after creation #
    ############################################################################
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})