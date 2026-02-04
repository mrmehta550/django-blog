
from django.shortcuts import render
from blog.models import Category,Blog
from assignments.models import About

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
