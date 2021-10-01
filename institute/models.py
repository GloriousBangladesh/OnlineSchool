from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
from django.db.models.signals import post_save
from django.dispatch import receiver 


class Institute(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institute_type = models.CharField(("Institute Type"), blank=True, max_length=50)
    institute_phone_number = models.CharField(("Phone Number"), blank=True, max_length=20)
    institute_short_desc = tinymce_models.HTMLField()
    profile_img = models.ImageField(upload_to = f"media/institute/profile_imgs/", null=True)

    def __str__(self):
        return f"{self.user.username}-({self.institute_type})"

class InstituteClass(models.Model):
    user_institute = models.ForeignKey(User, on_delete=models.CASCADE)
    class_no = models.CharField(("Class"), max_length=50)

    def __str__(self):
        return f"class {self.class_no} - {self.user_institute}"

class Subject(models.Model):
    subject_of_institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    subject_of = models.ForeignKey(InstituteClass, on_delete=models.CASCADE)
    subject_name = models.CharField(("Subject"), max_length=50, null=False)

    def __str__(self):
        return f"{self.subject_name}-{self.subject_of}"

class Applicant(models.Model):
    applicant_name = models.CharField(("Applicant"), max_length=50)
    applicant_email = models.EmailField(("Email"), max_length=254)
    previous_institute = models.CharField(("Previous Institute"), max_length=50, default=None, blank=True)
    previous_class = models.CharField(("Previous Class"), max_length=50, default=None, blank=True)
    applied_to = models.ForeignKey(Institute, on_delete=models.CASCADE)
    applied_class = models.ForeignKey(InstituteClass, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(("Applied On"), auto_now_add=True)

    def __str__(self):
        return f"{self.applicant_name}[{self.applied_on}]"

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fathers_name = models.CharField(("Fathers Name"), max_length=150)
    mothers_name = models.CharField(("Mothers Name"), max_length=150)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    of_class = models.ForeignKey(InstituteClass, on_delete=models.CASCADE)
    roll = models.IntegerField(("Roll"))

    def __str__(self):
        return f"{self.user.username}"

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    works_in = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    phone_number = models.CharField(("Phone Number"), max_length=15)
    of_class = models.ForeignKey(InstituteClass, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Notice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notice_title = models.CharField(("Title"), max_length=250)
    notice_content = tinymce_models.HTMLField()
    notice_img = models.ImageField(upload_to = f"media/institute/Notice_imgs/", null=True)
    created_on = models.DateTimeField(("Created On"), auto_now_add=True)

    @property
    def img_url(self):
        if self.notice_img and hasattr(self.notice_img, 'url'):
            return self.notice_img.url

    def __str__(self):
        return f"{self.notice_title} [{self.created_on}]"

        class Meta:
            ordering = ['-created_on']
    

