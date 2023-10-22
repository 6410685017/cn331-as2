from django.test import TestCase
from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from .models import Student, Subject, SubjectStudentList
from .views import sublist, enroll
from users.views import remove

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
        user1 = User.objects.create_user(username='0000', password='passcn331')
        student = User.objects.get(student='0000', id=0, is_staff=False)
        # User.objects.get()
        self.student1 = Student.objects.create(user=student.username, s_id=0)
        self.subject = Subject.objects.create(
            sub_id='CN202',
            name='Data Structure and Algorithm I',
            semester=1,
            year=2023,
            capacity=3,
            status=True
        )
        
        user1.save()
        

        self.sublist_url = reverse('regist:sublist')
        self.enroll_url = reverse('regist:enroll', args=[self.subject])
        self.remove_url = reverse('users:remove', args=[self.subject])
        self.client.login(username=user1.username, password=user1.password)

    def test_sublist(self):
        c = Client()
        response = c.get(self.sublist_url)
        self.assertCountEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'regist/sublist.html')

#     def test_enroll(self):
#         c = Client()
#         response = c.get(self.enroll_url)

#         self.assertCountEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'regist/sublist.html') 
    
#     def test_remove(self):
#         c = Client()
#         response = c.get(self.remove_url)

#         self.assertCountEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'users/index.html') 
    

 
# class TestModel(TestCase):
#     def setUp(self):
#         user1 = User.objects.create_user(username='0000', password='passcn331')
#         self.student1 = Student.objects.create(user=user1.username, s_id=0)
#         self.subject = Subject.objects.create(
#             sub_id='CN101',
#             name='INTRODUCTION TO COMPUTER PROGRAMMING',
#             semester=1,
#             year=2023,
#             capacity=3,
#             status=True
#         )
#         self.subjectstudentList = SubjectStudentList.objects.create(students=self.student1, subject=self.subject)
#         user1.save()

#     def test_student_str(self):
#         self.assertEquals(self.student1.__str__(), self.student1.user)

#     def test_subject_str(self):
#         self.assertEquals(self.subject.__str__(), self.subject.sub_id + ' ' + self.subject.sub_name)

#     def test_subjectstudent_str(self):
#         self.assertEquals(self.subjectstudentList.__str__(), self.student1.user + ' ' 
#                           + self.subject.sub_id + ' ' + self.subject.sub_name)
    