from django import forms
from .models import Blogs
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class BlogForm(forms.ModelForm):
    class Meta:
        model=Blogs
        fields=['text','photo']

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username','email','password1','password2')
