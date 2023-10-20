from http import client
from urllib import response
from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve
from regist.views import sublist, enroll
from .models import Student, Subject, SubjectStudentList

import json
from django.contrib.auth.models import User


# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_sublist_urls_is_resolved(self):
        url = reverse('regist:sublist')
        print(resolve(url))
        self.assertEqual(resolve(url).func,sublist)

    def test_enroll_urls_is_resolved(self):
        url = reverse('regist:enroll',args=[1])
        print(resolve(url))
        self.assertEqual(resolve(url).func,enroll)

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()

        self.username = 'testuser'
        self.password = 'cn331'
        self.email = 'user1@cn331.com'
        self.first = 'Test'
        self.last = 'User'
        self.credentials = {
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'first_name': self.first,
            'last_name': self.last }
        self.new_user = User.objects.create_user(**self.credentials)

        self.student = Student.objects.create(username=self.username,first=self.first, last=self.last)
        self.subject = Subject.objects.create(
            sub_id='CN331',
            sub_name='Sofeware Engineering',
            semester=1,
            year=2566,
            capacity=2,
            status=True
        )
        self.subjectstudentList = SubjectStudentList.objects.create(student=self.student, subject=self.subject)

        self.sublist_url = reverse('regist:sublist')
        self.enroll_url = reverse('regist:enroll', args=[self.subject])
    

        self.client.login(username=self.username, password=self.password)


    def test_sublist(self):
        response = self.client.get(self.sublist_url)

        self.assertCountEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'regist/sublist.html')

    def test_enroll(self):
        response = self.client.get(self.enroll_url)

        self.assertCountEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'regist/sublist.html') 

 
class TestModel(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            user = 'testuser',
            s_id = '0001',
        )

        self.subject = Subject.objects.create(
            sub_id='CN331',
            sub_name='Software Engineering',
            semester=1,
            year=2566,
            capacity=2,
            status=True
        )

        self.subjectstudentList = SubjectStudentList.objects.create(
            student = self.student,
            subject = self.subject
        )
    
    def test_student_str(self):
        self.assertEquals(self.student.__str__(), self.student.user)

    def test_subject_str(self):
        self.assertEquals(self.subject.__str__(), self.subject.sub_id + ' ' + self.subject.sub_name)

    def test_subjectstudent_str(self):
        self.assertEquals(self.subjectstudentList.__str__(), self.student.user + ' ' + self.subject.sub_id + ' ' + self.subject.sub_name)
    
