from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import index, login_view, logout_view, remove
from regist.models import Student, Subject
# from regist.views import enroll

# Create your tests here.
class TestUrl(SimpleTestCase):
    def test_index(self):
        url = reverse('users:index')
        self.assertEqual(resolve(url).func, index)

    def test_login(self):
        url = reverse('users:login')
        self.assertEqual(resolve(url).func, login_view)

    def test_logout(self):
        url = reverse('users:logout')
        self.assertEqual(resolve(url).func, logout_view)
    
    # def test_remove(self):
    #     url = reverse('users:index')
    #     self.assertEqual(resolve(url).func, remove, login_view) 
    

class TestViews(TestCase):
    def test_not_login(self):
        c = Client()
        response = c.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_login_success(self):
        c = Client()
        url = reverse('users:login')
        response = c.post(url, {
            'username': '0000',
            'password': 'passcn331'
        })

        self.assertEqual(response.status_code, 200)

    def test_login_unsuccess(self):
        url = reverse('users:login')
        response = self.client.post(url, {
            'username': '0000',
            'password': 'wrongpass'
        })

        self.assertEqual(response.status_code, 200)
   
    def test_logout_is_success(self):
        url = reverse("users:logout")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
    
    # def test_removesubject(self):
    #     response = self.client.post(self.removesubject_url)

    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'regist/sublist.html')

    # def test_removesubject_did_not_regist(self):
    #     subject = Subject.objects.create(
    #         sub_id='CN331',
    #         sub_name='Software Engineering',
    #         semester=1,
    #         year=2023,
    #         capacity=2,
    #         status=True
    #     )
    #     url = reverse('users:index', args=[subject.sub_id])
    #     response = self.client.post(url)

    #     self.assertEqual(response.status_code, 400)
    #     self.assertTemplateUsed(response, 'users/index.html')

    # def test_removesubject_get(self):
    #     response = self.client.get(self.remove_url)

    #     self.assertEqual(response.status_code, 400)
    #     self.assertTemplateUsed(response, 'regist/sublist.html')