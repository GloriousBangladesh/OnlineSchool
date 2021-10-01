from django.urls import path 
 
from . import views 
  
urlpatterns = [
    path('sign-in/', views.signIn, name='sign_in_teacher_view'),
    path('index/', views.index, name="index_teacher_view"),
    path('exam/', views.exam, name="exam_teacher_view"),
    path('classes/', views.classes, name="classes_teacher_view"),
    path('post-feed/', views.post_feed, name="post_feed_view"),
    path('students/', views.students, name="teacher_students_view"),
    path('sign-out/', views.signOut, name="institute_signOut_view"),
    path('<id>/delete', views.delete_post, name="teacher_post_delete_view")
]
