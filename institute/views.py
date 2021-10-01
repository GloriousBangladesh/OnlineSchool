import random
from django import forms 
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewUser, InstituteProfileForm, TeacherProfileForm, NoticeForm, AddClassForm
from student.forms import StudentProfileForm, CreateNewUserStudent
from teacher.forms import CreateNewUserTeacher
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .models import Student, Teacher, Notice, InstituteClass, Subject, Applicant, Institute
from teacher.models import Post


def register(request):
    user_register_form = CreateNewUser()
    user_profile_form = InstituteProfileForm()
    registered = False
    if request.method == "POST":
        user_register_form = CreateNewUser(data=request.POST)
        if request.FILES:
            user_profile_form = InstituteProfileForm(request.POST, request.FILES)
            print('works', request.FILES)
        else:
            user_profile_form = InstituteProfileForm(data=request.POST)
        if user_register_form.is_valid() and user_profile_form.is_valid():
            user = user_register_form.save()
            profile = user_profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            return redirect('institute_sign_in_view')
    return render(request, "institute_templates/institution-register.html", context={'user_register_form':user_register_form, 'user_profile_form':user_profile_form})

def sign_in(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('institute_index_view')
    
    return render(request, "institute_templates/login.html", context={'form':form})

@login_required(login_url="institute/")
def sign_out(request):
    logout(request)
    return redirect('index_landing_page')

@login_required(login_url="institute/")
def index(request):
    user = request.user
    institute = Institute.objects.get(user=user)
    total_students = len(Student.objects.all().filter(institute=institute))
    total_teachers = len(Teacher.objects.all().filter(works_in=request.user))
    return render(request, "institute_templates/index_da.html", context={'institute':user,'total_students':total_students, 'total_teachers':total_teachers})

@login_required(login_url="institute/")
def teachers(request):
    institute = Institute.objects.get(user=request.user)
    classes = InstituteClass.objects.all().filter(user_institute=request.user)
    teachers = Teacher.objects.all()

    TeacherProfileForm.base_fields['of_class'] = forms.ModelChoiceField(required=True,
    queryset=InstituteClass.objects.all().filter(user_institute=request.user).order_by('id'), widget=forms.Select(attrs={'class':'mb-3', 'id':'_class'}))

    TeacherProfileForm.base_fields['subject'] = forms.ModelChoiceField(required=True,
    queryset=Subject.objects.all().filter(subject_of_institute=institute).order_by('id'), widget=forms.Select(attrs={'class':'mb-3', 'id':'subject'}))

    teacher_user_form = CreateNewUserTeacher()
    teacher_profile_form = TeacherProfileForm()
    if request.method == "POST":
        teacher_profile_form = TeacherProfileForm(
            data=request.POST,
        )
        teacher_user_form = CreateNewUserTeacher(
            data=request.POST,
        )
        if teacher_profile_form.is_valid() and teacher_user_form.is_valid():

            password = hex(random.randint(1000000,100000000))[1:]
            user = User.objects.create(username=request.POST.get('username'), email=request.POST.get('email'))
            user.set_password(password)
            user.save()

            profile = teacher_profile_form.save(commit=False)
            profile.user = user
            profile.works_in = request.user
            profile.save()
        
            #mail content
            subject = f'Login Information for {user.username}'
            message = f'''{user.username}'s username: {user.username} \n {user.username}'s password: {password}'''
            # send email
            send_mail(
                subject= subject,
                message= message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[f'{user.email}'],
                fail_silently=False,
            )
    return render(request, "institute_templates/teachers_da.html",
                context={'teacher_profile_form':teacher_profile_form,
                         'institute':request.user,
                         'teacher_user_form':teacher_user_form,
                         'teachers':teachers,
                         'classes':classes})

@login_required(login_url="institute/")
def classes(request):
    add_class_form = AddClassForm()
    classes = InstituteClass.objects.all().filter(user_institute=request.user)
    subjects = Subject.objects.all()
    if request.method == "POST" and 'add_class' in request.POST:
        add_class_form = AddClassForm(data=request.POST)
        if add_class_form.is_valid():
            added_class = add_class_form.save(commit=False)
            added_class.user_institute = request.user
            added_class.save()
    if request.method == "POST" and 'add_subject' in request.POST:
            institute = Institute.objects.get(user=request.user)
            Class = InstituteClass.objects.get(id=request.POST.get('_class'))
            subject = Subject.objects.create(subject_of_institute=institute, subject_of=Class, subject_name=request.POST.get('subject_name'))
            subject.save()


    return render(request, "institute_templates/classes.html",
                    context={'institute':request.user,
                             'classes':classes, 
                             'subjects':subjects, 
                             'add_class_form':add_class_form})

@login_required(login_url="institute/")
def students(request):

    institute = Institute.objects.get(user=request.user)

    applicants = Applicant.objects.all().filter(applied_to=request.user.id)
    classes = InstituteClass.objects.all().filter(user_institute=request.user)
    students = Student.objects.all().filter(institute=institute)

    student_user_form = CreateNewUserStudent()
    StudentProfileForm.base_fields['institute'] = forms.ModelChoiceField(required=True, queryset=Institute.objects.all().filter(user=request.user).order_by('id'), 
    widget=forms.Select(attrs={'class':'mb-3'}))
    StudentProfileForm.base_fields['of_class'] = forms.ModelChoiceField(required=True, queryset=InstituteClass.objects.all().filter(user_institute=request.user).order_by('id'), 
    widget=forms.Select(attrs={'class':'mb-3'}))
    student_add_form = StudentProfileForm()

    if request.method == "POST":
        student_user_form = CreateNewUserStudent(data=request.POST)
        student_add_form = StudentProfileForm(data=request.POST)
        if student_add_form.is_valid() and student_user_form.is_valid():
            # auto password
            password = hex(random.randint(1000000,100000000))[1:]

            student = User.objects.create(username=request.POST.get('username'), email=request.POST.get('email'))
            student.set_password(password)
            student.save()


            # create student
            student_profile = student_add_form.save(commit=False)
            student_profile.user = student
            student_profile.save()


            #mail content
            subject = f'Login Information for {student.username}'
            message = f'''{student.username}'s username: {student.username} \n {student.username}'s password: {password}'''
            # send email
            send_mail(
                subject= subject,
                message= message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[f'{student.email}'],
                fail_silently=False,
            )
            
    return render(request, "institute_templates/students_da.html",
        context={'student_add_form':student_add_form ,
                'institute':request.user,
                'applicants':applicants,
                'classes':classes,
                'students':students,
                'student_user_form':student_user_form})

@login_required(login_url="institute/")
def notice(request):
    notice_form = NoticeForm()
    notices = Notice.objects.all().filter(user=request.user)
    if request.method == "POST":
        notice_form = NoticeForm(data=request.POST)
        if request.FILES:
            notice_form = NoticeForm(request.POST, request.FILES)
        else:
            notice_form = NoticeForm(data=request.POST)
        if notice_form.is_valid():
            notice = notice_form.save(commit=False)
            notice.user = request.user
            notice.save()
    return render(request, "institute_templates/notice_da.html", context={'notice_form':notice_form, 'notices':notices, 'institute':request.user})

@login_required(login_url="institute/")
def delete_notice(request, id):
    notice = get_object_or_404(Notice, id = id)
    notice.delete()
    return redirect('institute_notice_view')

@login_required(login_url="institute/")
def all_notices(request):


    institute_notice = Notice.objects.all()
    teacher_post = Post.objects.all()

    # print(institute_notice)
    # print(teacher_post)

    return render(request, 'institute_templates/notices.html',
                context={'institute_notice':institute_notice,
                         'teacher_post':teacher_post})