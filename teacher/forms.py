from django import forms 
from tinymce.widgets import TinyMCE
from .models import Post
from django.contrib.auth.models import User


class CreateNewUserTeacher(forms.ModelForm):

    username = forms.CharField(required=True, label="Teacher Name",
    widget=forms.TextInput(attrs={'PlaceHolder':'Institute Name', 'class':'mb-3'}))

    email = forms.EmailField(required=True, label="Teacher Email",
    widget=forms.TextInput(attrs={'PlaceHolder':'Email Address', 'class':'mb-3'}))

    class Meta:
        model = User
        fields = ['username', 'email']




class PostForm(forms.ModelForm):

    content = forms.CharField(required=True, label='Content', widget=TinyMCE(attrs={'cols': 80, 'rows': 12,}))
    
    class Meta:
        model = Post
        fields = ("of_class","content",)
