from django.db import models
#for date_posted
from django.utils import timezone
#importing users to this
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # auto_now=True, when need to change time, auto_now_add = when post was created 
    author = models.ForeignKey(User, on_delete=models.CASCADE) # on_delete == when user is deleted, then also post is deleted

    def __str__(self):
        return self.title