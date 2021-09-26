from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.
def register(request): # views.py functions take always 'request' as argument
    # django already has user registration form
    # Method 'POST' is defined in login.html with button type as 'submit'
    if request.method == 'POST':
        #takes form 'POST' method contents from login.html and modified UserRegisterForm function as argument
        form = UserRegisterForm(request.POST)
        if form.is_valid(): 
            form.save() #hashes password, and saves the form data to User model in django.contrib.auth.models
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            messages.success(request, f'You are now able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form}) # render's first argument always is request

# Require logged in user before this view can be shown
# So that means if not logged in then routes to generic login route
# This has to be defined in the settings as 'LOGIN_URL'
# Without defining, redirects to 'accounts/login', but after defining 'LOGIN_URL = 'login'' user gets directed to our url named 'login'
@login_required
def profile(request):
    # 'POST' is defined in profile.html as button type 'submit'
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                    request.FILES, 
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

