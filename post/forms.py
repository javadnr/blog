from django import forms
from .models import Post,Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image','title','description','category','trend'] 
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','body']
        
class LogInForm(AuthenticationForm):
    class Meta:
        model : User
        fields = ['username','password']
        
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username']
                        

        
        
        