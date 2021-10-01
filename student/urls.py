from django.urls import path 
 
from . import views

urlpatterns = [
    path('apply/', views.apply, name='student_apply_view'),
    path('sign-in', views.signIn, name="student_signin_view"),
    path('sign-out/', views.signOut, name="Student_signout_view"),
    path('class-mates/', views.classmates, name="student_classmate_view"),
    path('online-classes', views.onlineclasses, name="student_OnlineClasses_view"),
    path('exam', views.exam, name="student_exam_view"),
    path('my-profile/', views.myprofile, name="student_myprofile_view"),
    path('index/', views.index, name="student_index_view"),
    path('notes/', views.notes, name="student_notes_view"),
    path('post-feed', views.post_feed, name="student_post_feed_view"),
]