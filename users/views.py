from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request): # views functions take always request as argument
    #django already has user registration form
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form}) # renders first argument always is request
