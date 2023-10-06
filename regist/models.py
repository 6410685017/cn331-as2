from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    s_id = models.IntegerField()
    

    def __str__(self):
        return f'ID: {self.s_id} ,Username {self.user.username}'
    
class Subject(models.Model):
    sub_id = models.CharField(max_length=5, primary_key='True')
    sub_name = models.CharField(max_length=64)
    capacity  = models.IntegerField()
    status = models.BooleanField()
    # semester = models.IntegerField()
    # year = models.IntegerField()

    def __str__(self):
        return f'{self.sub_id}: {self.sub_name}'

class SubjectStudentList(models.Model):
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE, primary_key=True)
    students = models.ManyToManyField(Student, blank=True)

