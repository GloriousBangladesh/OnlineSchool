from django.db import models 
from django.contrib.auth.models import User
from institute.models import InstituteClass
from teacher.models import Exam
from tinymce import models as tinymce_models

# Create your models here.


class StudentNote(models.Model):
    user_student = models.ForeignKey(User, verbose_name=("Student"), on_delete=models.CASCADE)
    of_class = models.ForeignKey(InstituteClass, on_delete=models.DO_NOTHING)
    content = tinymce_models.HTMLField()
    posted_on = models.DateTimeField(("Posted On"), auto_now_add=True)

    class Meta:
        verbose_name = ("Note")
        verbose_name_plural = ("Notes")

    def __str__(self):
        return f"{self.user_student}-{self.posted_on}"


class StudentPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    of_class = models.ForeignKey(InstituteClass, on_delete=models.DO_NOTHING)
    post_content = tinymce_models.HTMLField()
    created_on = models.DateTimeField(("Created On"), auto_now_add=True)

    def __str__(self):
        return f"{self.user} [{self.created_on}]"

        class Meta:
            ordering = ['-created_on']


class ExamAns(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam_qus = models.ForeignKey(Exam, on_delete=models.DO_NOTHING)

    answer = models.FileField(("Exam Answer"), upload_to=f'exam/answers')
    posted_on = models.DateField(("Posted On"), auto_now_add=True)

    @property
    def file_url(self):
        if self.answer and hasattr(self.answer, 'url'):
            return self.answer.url

    class Meta:
        verbose_name = ("ExamAns")
        verbose_name_plural = ("ExamAns's")

    def __str__(self):
        return f"{self.user}-{self.posted_on}"