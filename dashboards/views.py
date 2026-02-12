from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from blog.models import Blog,Category
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm

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

