from django.shortcuts import render, redirect 
from .forms import InstituteApplicationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .forms import NoteForm, PostForm, ExamAnsForm
from .models import StudentNote, StudentPost
from institute.models import Student
from teacher.models import Exam

# Create your views here.
def apply(request):
    application_form = InstituteApplicationForm()
    if request.method == "POST": 
        application_form = InstituteApplicationForm(data=request.POST)
        if application_form.is_valid():
            application_form.save()
        return redirect('index_landing_page')
    #else:
    return render(request, "student_templates/student-register.html", context={'form':application_form})

def signIn(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('student_index_view')
    
    return render(request, "student_templates/Student_signin.html", context={'form':form})

@login_required(login_url="student/")
def signOut(request):
    logout(request)
    return redirect('index_landing_page')

@login_required(login_url="student/")
def classmates(request):
    student = request.user
    class_mates = Student.objects.all().filter(institute=student.student.institute)
    return render(request, "student_templates/classmates_ds.html", 
                  context={'student': student,
                            'class_mates':class_mates,
                            })

@login_required(login_url="student/")
def onlineclasses(request):
    return render(request, "student_templates/online_classes_ds.html", context={'student':request.user})

@login_required(login_url="student/")
def exam(request):
    student = request.user

    exams = Exam.objects.all()

    ExamAnsForm.base_fields['exam_qus'] = forms.ModelChoiceField(required=True,
    queryset=Exam.objects.all().filter(of_class=student.student.of_class).order_by('id'), widget=forms.Select(attrs={'class':'mb-3', 'id':'subject'}))
    form = ExamAnsForm()

    if request.method == "POST":
        exam_ans = ExamAnsForm(request.POST, request.FILES)
        if exam_ans.is_valid():
            exam_ans = exam_ans.save(commit=False)
            exam_ans.user = student
            exam_ans.save()

    return render(request, "student_templates/exam_ds.html",
                  context={'student':student,
                            'form':form,
                            'exams':exams})

@login_required(login_url="student/")
def myprofile(request):
    return render(request, "student_templates/profile_student.html")

@login_required(login_url="student/")
def index(request):
    return render(request, "student_templates/index_ds.html", context={'student':request.user})

@login_required(login_url="student/")
def notes(request):
    notes = StudentNote.objects.all()


    form = NoteForm()
    if request.method == "POST":
        note = NoteForm(request.POST)
        if note.is_valid():
            note = note.save(commit=False)
            note.user_student = request.user
            note.of_class = request.user.student.of_class
            note.save()       
    return render(request, "student_templates/notes_ds.html",
                  context={'student':request.user,
                           'form':form,
                           'notes':notes})

@login_required(login_url="student/")
def post_feed(request):
    student = request.user

    posts = StudentPost.objects.all().filter(of_class=student.student.of_class)

    form = PostForm()
    if request.method == "POST":
        post = PostForm(request.POST)
        if post.is_valid():
            post = post.save(commit=False)
            post.user = student
            post.of_class = student.student.of_class
            post.save()
    return render(request, "student_templates/post_to_feed_ds.html",
                  context={'student':student,
                           'form':form,
                           'posts':posts})