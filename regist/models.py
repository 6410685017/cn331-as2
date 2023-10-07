from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    s_id = models.PositiveIntegerField()
    
    def __str__(self):
        return f'ID: {self.s_id} ,Username {self.user.username}'
    
class Subject(models.Model):
    sub_id = models.CharField(max_length=5, primary_key='True')
    sub_name = models.CharField(max_length=64)
    capacity  = models.PositiveIntegerField()
    status = models.BooleanField()
    semester = models.PositiveIntegerField()
    year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.sub_id} {self.sub_name}'

class SubjectStudentList(models.Model):
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE, primary_key=True)
    students = models.ManyToManyField(Student, blank=True)
    
    def __str__(self):
        return f'{self.subject.sub_id} {self.subject.sub_name}'

