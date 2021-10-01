from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from institute.models import InstituteClass, Teacher, Student, Subject
from .models import Post, Exam
from .forms import PostForm
from django import forms
 
# Create your views here. 
  

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
                return redirect('index_teacher_view')

    return render(request, "teacher_templates/signin_teacher.html", context={'form':form})

@login_required(login_url="teacher/")
def signOut(request):
    logout(request)
    return redirect('sign_in_teacher_view')

@login_required(login_url="teacher/")
def index(request):
    return render(request, 'teacher_templates/index_dt.html', context={'teacher':request.user})

@login_required(login_url="teacher/")
def exam(request):

    teacher = Teacher.objects.get(user=request.user)
    exams = Exam.objects.all().filter(of_class=teacher.of_class)

    if request.method == "POST":
        
        Exam.objects.create(user_teacher=request.user,
                            of_class=InstituteClass.objects.get(id=request.POST.get('class')),
                            subject=Subject.objects.get(id=request.POST.get('subject')),
                            exam_day=request.POST.get('date'),
                            start_time=request.POST.get('start_time'),
                            end_time=request.POST.get('end_time'))

    return render(request, 'teacher_templates/exam_dt.html', 
                  context={'teacher':request.user,
                           'user_teacher':teacher,
                           'exams':exams})

@login_required(login_url="teacher/")
def classes(request):
    return render(request, 'teacher_templates/classes_dt.html', context={'teacher':request.user})

@login_required(login_url="teacher/")
def post_feed(request):
    teacher = Teacher.objects.get(user=request.user)
    classes = InstituteClass.objects.select_related('user_institute').filter(user_institute=teacher.works_in)
    print(classes)
    posts = Post.objects.all().filter(user_teacher=request.user)


    PostForm.base_fields['of_class'] =forms.ModelChoiceField(required=True,
    queryset=classes, widget=forms.Select(attrs={'class':'mb-3'}))

    post_form = PostForm()

    if request.method == "POST":
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user_teacher = request.user
            post.save()
    return render(request, 'teacher_templates/post_to_feed_dt.html', context={'classes':'classes', 'posts':posts, 'teacher':request.user, 'post_form':post_form})

@login_required(login_url="institute/")
def delete_post(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('post_feed_view')

@login_required(login_url="teacher/")
def students(request):
    print()
    teacher_class = Teacher.objects.get(user=request.user)
    classes = InstituteClass.objects.all()
    students = Student.objects.all()
    return render(request, 'teacher_templates/students.html',
                  context={'teacher':request.user,
                            'classes':classes,
                            'teacher_class': teacher_class,
                            'students':students})