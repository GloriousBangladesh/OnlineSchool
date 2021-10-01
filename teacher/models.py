from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
from institute.models import InstituteClass, Subject, Institute
  
# Create your models here.
class Post(models.Model):
    user_teacher = models.ForeignKey(User, verbose_name=("Teacher"), on_delete=models.CASCADE)
    of_class = models.ForeignKey(InstituteClass, on_delete=models.CASCADE)
    content = tinymce_models.HTMLField()
    posted_on = models.DateTimeField(("Posted On"), auto_now_add=True)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return f"{self.user_teacher}-{self.posted_on}"


class Exam(models.Model):
    user_teacher =  models.ForeignKey(User, verbose_name=("Teacher"), on_delete=models.CASCADE)
    of_class = models.ForeignKey(InstituteClass, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam_day = models.DateField(("Day"))
    start_time = models.TimeField(("Start"))
    end_time = models.TimeField(("End"))
    posted_on = models.DateTimeField(("Posted On"), auto_now_add=True)
    

    class Meta:
        verbose_name = ("Exam")
        verbose_name_plural = ("Exams")

    def __str__(self):
        return f"{self.subject}-{self.of_class}-{self.user_teacher}"

