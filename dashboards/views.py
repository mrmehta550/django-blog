from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from blog.models import Blog,Category
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, BlogPostForm
from django.template.defaultfilters  import slugify

@login_required(login_url='login') #This is decorator
def dashboard(request):
    category_count = Category.objects.count()
    blogs_count = Blog.objects.count()

    context = {
        'category_count': category_count,
        'blogs_count': blogs_count,
    }
    return render(request, 'dashboard/dashboard.html', context)

def categories(request):
    return render(request, 'dashboard/categories.html')

def blogs(request):
    return render(request, 'dashboard/blog.html')

def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    forms = CategoryForm()
    context = {
        'form': forms,
    }
    return render(request, 'dashboard/add_category.html', context)

def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm(instance=category)

    context = {
        'form': form,
        'category': category,   # 👈 THIS WAS MISSING
    }

    return render(request, 'dashboard/edit_category.html', context)

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')

def posts(request):
    posts = Blog.objects.all()#fetch all posts from data bd
    context = {
        'posts' : posts
    }
    return render(request, 'dashboard/posts.html', context)

def add_posts(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-'+str(post.id)
            post.save()
            return redirect('posts')
        else:
            print('form is invalid')
            print(form.errors)
    form = BlogPostForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_post.html',context)

def edit_post(request):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-'+str(post.id)
            post.save()
            return redirect('posts')
    form = BlogPostForm(instance=post)
    context = {
        'form':form,
        'post':post
    }

    return render(request, 'dashboard/e+dit_post.html', context)

def delete_post(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('posts')
