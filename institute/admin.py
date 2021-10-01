from django.contrib import admin


from .models import ( Institute,
                      InstituteClass,
                      Subject,
                      Applicant,
                      Student,
                      Teacher,
                      Notice,                 
)

# Register your models here.
admin.site.register(Institute)
admin.site.register(InstituteClass)
admin.site.register(Subject)
admin.site.register(Applicant)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Notice)




