from django.db import models

# Create your models here.
class InstituteType(models.Model):
    institute_type = models.CharField(("Institute Type"), max_length=50)

    def __str__(self):
        return self.institute_type
    
