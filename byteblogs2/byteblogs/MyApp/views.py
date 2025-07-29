from django.shortcuts import render,redirect
from MyApp.models import Blogs
from .Forms import BlogForm,UserRegisterForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def home(request):
        return render(request,'MyTemp/home.html')
def bloglist(request):
        blogs=Blogs.objects.all().order_by('-create_at')
        return render(request,'MyTemp/bloglist.html',{'blogs':blogs})
@login_required
def blogadd(request):
        if request.method=="POST":
               form =BlogForm(request.POST,request.FILES)
               if form.is_valid():
                      blog=form.save(commit=False)
                      blog.user=request.user
                      blog.save()
                      return redirect('bloglist')
        else:
          form=BlogForm()
        return render(request,'MyTemp/blogform.html',{'form':form})
@login_required
def blogedit(request,blog_id):
        blog=get_object_or_404(Blogs,pk=blog_id,user=request.user)
        if request.method=="POST":
          form =BlogForm(request.POST,request.FILES,instance=blog)
          if form.is_valid():
                blog=form.save(commit=False)
                blog.user=request.user
                blog.save()
                return redirect('bloglist')
        else:
              form =BlogForm(instance=blog)
        return render(request,'MyTemp/blogform.html',{'form':form})
@login_required
def blogDelete(request,blog_id):
        blog=get_object_or_404(Blogs,pk=blog_id,user=request.user)
        if request.method=="POST":
              blog.delete()
              return redirect('bloglist')
        return render(request,'MyTemp/blogDelete.html',{'blog':blog})

def Register(request):
        if request.method=="POST":
              form=UserRegisterForm(request.POST)
              if form.is_valid():
                    user=form.save(commit=False)
                    user.set_password(form.cleaned_data['password1'])
                    user.save()
                    login(request,user)
                    return redirect('bloglist')
        else:
              form=UserRegisterForm()
        return render(request,'Registration/register.html',{'form':form})

def AboutUs(request):
        return render(request,'MyTemp/AboutUs.html')
def ContactUs(request):
        return render(request,'MyTemp/Contactus.html')
