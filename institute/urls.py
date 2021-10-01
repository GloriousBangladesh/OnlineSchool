from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('register/', views.register, name='institute_register_view'),
    path('sign-in/', views.sign_in, name='institute_sign_in_view'),
    path('index/', views.index, name="institute_index_view"),
    path('teachers/', views.teachers, name="institute_teachers_view"),
    path('classes/', views.classes, name="institute_classes_view"),
    path('students/', views.students, name="institute_students_view"),
    path('notice/', views.notice, name="institute_notice_view"),
    path('sign-out/', views.sign_out, name="institute_logout_view"),
    path('<id>/delete', views.delete_notice, name="institute_notice_delete_view"),
    path('all-notices/', views.all_notices, name="institute_all_notices_view")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()