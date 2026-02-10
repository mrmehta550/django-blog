
from django.contrib import admin
from django.urls import path,include
from.import views
from django.conf.urls.static import static
from django.conf import settings
from blog import views as BlogsView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('category/', include('blog.urls')),
    path('blog/<slug:slug>/', BlogsView.blog, name='blog'),
    # search endpoint
    path('blogs/search/', BlogsView.search, name='search'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),


] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
