from django.db import models
from django.contrib.auth.models import User


# ps. any new models need to be registered at '<app>/admin.py'
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # currently image file remains in the file system when profile is deleted. 
    # might want to implement 'on_delete.CASCADE' but on ImageField --> https://djangosnippets.org/snippets/10638/

    def __str__(self):
        return f'{self.user.username} Profile'
