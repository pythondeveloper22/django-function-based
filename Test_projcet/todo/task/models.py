from django.db import models


# Create your models here.
class Student(models.Model):
    student_name=models.CharField(max_length=70)
    contact_number=models.IntegerField()
    student_address=models.CharField(max_length=80)
