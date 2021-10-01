from django import forms 
from homeapp.models import InstituteType 
from tinymce.widgets import TinyMCE
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from institute.models import Applicant, Institute, InstituteClass, Student
from .models import StudentNote, StudentPost, ExamAns

class InstituteApplicationForm(forms.ModelForm):
    applicant_name = forms.ModelChoiceField(required=True,
    queryset=InstituteType.objects.all().order_by('institute_type'), widget=forms.Select(attrs={'class':'mb-3'}))

    applicant_name = forms.CharField(required=True, label="Student Name",
    widget=forms.TextInput(attrs={'PlaceHolder':'name', 'class':'mb-3'}))

    applicant_email = forms.EmailField(required=True, label="Students Email",
    widget=forms.TextInput(attrs={'PlaceHolder':'email', 'class':'mb-3'}))

    previous_institute = forms.CharField(max_length=100, required=False, label="Previous Institute",
    widget=forms.TextInput(attrs={'PlaceHolder':'prev_institute', 'class':'mb-3'}))

    previous_class = forms.CharField(label="Previous Class", max_length=15, required=False,
    widget=forms.TextInput(attrs={'PlaceHolder':'prev_class', 'class':'mb-3'}))

    applied_to = forms.ModelChoiceField(required=True, queryset=Institute.objects.all().order_by('id'), 
    widget=forms.Select(attrs={'class':'mb-3'}))
    
    applied_class = forms.ModelChoiceField(required=True, queryset=InstituteClass.objects.all().order_by('id'), 
    widget=forms.Select(attrs={'class':'mb-3'}))

    class Meta:
        model = Applicant
        fields = ['applicant_name', 'applicant_email', 'previous_institute', 'previous_class', 'applied_to', 'applied_class']


class CreateNewUserStudent(forms.ModelForm):

    username = forms.CharField(required=True, label="Username",
    widget=forms.TextInput(attrs={'PlaceHolder':'Username', 'class':'mb-3'}))

    email = forms.EmailField(required=True, label="Student Email",
    widget=forms.TextInput(attrs={'PlaceHolder':'Email Address', 'class':'mb-3'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class StudentProfileForm(forms.ModelForm):
    
    fathers_name = forms.CharField(label="Fathers Name", max_length=30, required=True,
    widget=forms.TextInput(attrs={'PlaceHolder':'Fathers Name', 'class':'mb-3'}))

    mothers_name = forms.CharField(label="Mothers Name", max_length=30, required=True,
    widget=forms.TextInput(attrs={'PlaceHolder':'Fathers Name', 'class':'mb-3'}))

    roll = forms.IntegerField(label="Roll", required=True,
    widget=forms.TextInput(attrs={'PlaceHolder':'Roll', 'class':'mb-3'}))

    class Meta:
        model = Student
        fields = ("fathers_name", "mothers_name", "institute", "of_class", "roll")


class NoteForm(forms.ModelForm):

    content = forms.CharField(max_length=500, required=True, label="Content",
    widget=TinyMCE(attrs={'cols': 80, 'rows': 12}))
    
    class Meta:
        model = StudentNote
        fields = ("content",)


class PostForm(forms.ModelForm):

    post_content = forms.CharField(max_length=500, required=True, label="Content",
    widget=TinyMCE(attrs={'cols': 80, 'rows': 12}))
    
    class Meta:
        model = StudentPost
        fields = ("post_content",)

class ExamAnsForm(forms.ModelForm):

    class Meta:
        model = ExamAns
        fields = ("exam_qus", "answer")



    
