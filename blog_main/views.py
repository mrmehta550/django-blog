
from django.shortcuts import render
from blog.models import Category,Blog
from assignments.models import About
from .forms import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def home(request):
    featured_posts = Blog.objects.filter(is_featured=True,  status="Published").order_by('-updated_at')
    posts = Blog.objects.filter(is_featured=False, status="Published")
    
    try:
        about = About.objects.get() # if about have some data then print it otherwise print none.
    except:
        about = None
    
    context = {
        'featured_posts': featured_posts,
        'posts' : posts,
        'about' : about, # context is going.
    }
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  # ✅ redirect to login page
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('home')