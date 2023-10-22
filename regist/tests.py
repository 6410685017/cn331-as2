from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from .models import Student, Subject
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

    def test_remove_urls_is_resolved(self):
        url = reverse('users:remove',args=[1])
        print(resolve(url))
        self.assertEqual(resolve(url).func,remove)

class TestViews(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser', password='passcn331')
        self.student1 = Student.objects.create(user=self.user1, s_id=0)
        self.cn202 = Subject.objects.create(
            sub_id='CN202',
            sub_name='Data Structure and Algorithm I',
            semester=1,
            year=2023,
            capacity=3,
            status=True
        )
        self.client.login(username='testuser', password='passcn331')

    def test_sublist(self):
        response = self.client.get(reverse('regist:sublist'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sublist.html')

        self.assertContains(response, 'testuser')
        self.assertContains(response, '0')

    def test_enroll(self):
        response = self.client.get(reverse('regist:sublist'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sublist.html') 

    def test_remove(self):
        response = self.client.get(reverse('users:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html') 
    
