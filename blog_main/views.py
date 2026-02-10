
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
            form.save()
            return redirect('register.html')  # optional
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = auth.autheticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('home')
    form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')