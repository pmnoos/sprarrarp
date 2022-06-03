from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.forms.models import formset_factory

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'author'
        )
   
    def __str__(self):
        return self.title + "/n "  + self.author.username

   
    
   
