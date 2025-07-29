from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('bloglist', views.bloglist, name='bloglist'),
    path('blogadd', views.blogadd, name='blogadd'),
    path('<int:blog_id>/edit', views.blogedit, name='blogedit'),
    path('<int:blog_id>/delete', views.blogDelete, name='blogDelete'),
    path('register', views.Register, name='register'),
    path('about', views.AboutUs, name='about'),
    path('contact', views.ContactUs, name='contact'),
]
