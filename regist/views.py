from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from regist.models import Student, Subject, SubjectStudentList

# Create your views here.

def sublist(request):
    student = Student.objects.get(user_id=request.user)
    subjects = Subject.objects.all()
    data = {'student': student, 
            'subjects': subjects}
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'sublist.html', data)

def enroll(request, sub_id):
    student = Student.objects.get(user_id=request.user)
    sublist = SubjectStudentList.objects.get(subject_id=sub_id)
    sublist.students.add(student)

    subj = Subject.objects.get(sub_id=sub_id)
    subj.capacity -= 1
    if subj.capacity < 0:
        return render(request, 'sublist.html')
    subj.save()
    
    return HttpResponseRedirect(reverse('users:index'))