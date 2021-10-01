from django import forms
from homeapp.models import InstituteType
from tinymce.widgets import TinyMCE
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Institute, Teacher, InstituteClass, Subject, Notice

class CreateNewUser(UserCreationForm):

    username = forms.CharField(required=True, label="Institute Name",
    widget=forms.TextInput(attrs={'PlaceHolder':'Institute Name', 'class':'mb-3'}))

    email = forms.EmailField(required=True, label="Institute Email",
    widget=forms.TextInput(attrs={'PlaceHolder':'Email Address', 'class':'mb-3'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
 

class InstituteProfileForm(forms.ModelForm):

    institute_type = forms.ModelChoiceField(required=True,
    queryset=InstituteType.objects.all().order_by('institute_type'), widget=forms.Select(attrs={'class':'mb-3'}))

    institute_phone_number = forms.CharField(required=True, label="Institute Phone Number",
    widget=forms.TextInput(attrs={'PlaceHolder':'Phone Number', 'class':'mb-3'}))
        
    institute_short_desc = forms.CharField(max_length=500, required=False, label="About Institute",
    widget=TinyMCE(attrs={'cols': 80, 'rows': 4}))

    profile_img = forms.ImageField(required=False, label="Institute Image")

    class Meta:
        model = Institute
        fields = ['institute_type', 'institute_phone_number', 'institute_short_desc', 'profile_img']


class TeacherProfileForm(forms.ModelForm):

    phone_number = forms.CharField(required=True, label="Phone Number",
    widget=forms.TextInput(attrs={'PlaceHolder':'Phone Number', 'class':'mb-3', 'id':'phone_number'}))

    class Meta:
        model = Teacher
        fields = ['phone_number', 'of_class', 'subject']


class NoticeForm(forms.ModelForm):

    notice_title = forms.CharField(required=True, label="Title",
    widget=forms.TextInput(attrs={'PlaceHolder':'Title', 'class':'mb-3'}))

    notice_content = forms.CharField(max_length=500, required=True, label="Content",
    widget=TinyMCE(attrs={'cols': 80, 'rows': 12}))
    
    notice_img = forms.ImageField(required=False, label="Image")
    
    class Meta:
        model = Notice
        fields = ("notice_title", "notice_content", "notice_img")


class AddClassForm(forms.ModelForm):

    class_no = forms.CharField(label="Class Name", max_length=10, required=True, 
    widget=forms.TextInput(attrs={'PlaceHolder':'I ,II, III etc'}))
    
    class Meta:
        model = InstituteClass
        fields = ("class_no",)









    
