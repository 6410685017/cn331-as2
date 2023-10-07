from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from regist.models import Student, Subject, SubjectStudentList

# Create your views here.

def index(request):
    student = Student.objects.get(user_id=request.user)
    subjects = SubjectStudentList.objects.all()

    mysubject = []
    for subject in subjects:
        if student in subject.students.all():
            mysubject.append(subject)

    data = {'student': student, 
            'subjects': mysubject}
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'index.html', data)

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('users:index'))
        else:
            return render(request, 'login.html', {
                'message': 'Invalid credentials.'
            })

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return render(request, 'login.html', {
        'message': 'Logged out'
    })

def remove(request, sub_id):
    student = Student.objects.get(user_id=request.user)
    sublist = SubjectStudentList.objects.get(subject_id=sub_id)
    sublist.students.remove(student)
    
    subj = Subject.objects.get(sub_id=sub_id)
    subj.capacity += 1
    if subj.capacity < 0:
        return render(request, 'sublist.html')
    subj.save()

    return HttpResponseRedirect(reverse('users:index'))