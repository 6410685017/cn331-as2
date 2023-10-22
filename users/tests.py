from django.test import TestCase, SimpleTestCase
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.contrib.auth import authenticate
from .views import index, login_view, logout_view
from regist.models import Student


# Create your tests here.
class TestUrl(SimpleTestCase):
    def test_index_is_resolved(self):
        url = reverse('users:index')
        self.assertEqual(resolve(url).func, index)

    def test_login_is_resolved(self):
        url = reverse('users:login')
        self.assertEqual(resolve(url).func, login_view)

    def test_logout_is_resolved(self):
        url = reverse('users:logout')
        self.assertEqual(resolve(url).func, logout_view)

class TestViews(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser', password='passcn331')
        self.student1 = Student.objects.create(user=self.user1, s_id=0)
    
    def test_status_login(self):
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_is_success(self):
        response = self.client.post(reverse('users:login'), {
            'username': 'testuser',
            'password': 'passcn331'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:index'))

    def test_login_is_unsuccess(self):
        response = self.client.post(reverse('users:login'), {
            'username': 'testuser',
            'password': 'wrongpass'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('message' in response.context)
        self.assertEqual(response.context['message'], 'Invalid credentials.')
    
    def test_index_view_authenticated_user(self):
        response = self.client.post(reverse('users:login'), {
            'username': 'testuser',
            'password': 'passcn331'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:index'))
        user = authenticate(username='testuser', password='passcn331')
        self.assertTrue(user.is_authenticated)
    
    def test_logout_is_success(self):
        url = reverse('users:logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    