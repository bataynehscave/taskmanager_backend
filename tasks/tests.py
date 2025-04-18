from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status

class TaskTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='1234')
        self.client.login(username='test', password='1234')

    def test_register(self):
        res = self.client.post('/api/register/', {'username': 'new', 'password': '1234'})
        self.assertEqual(res.status_code, 201)

    def test_login(self):
        res = self.client.post('/api/login/', {'username': 'test', 'password': '1234'})
        self.assertIn('access', res.data)

    def test_create_task(self):
        self.client.force_authenticate(user=self.user)
        res = self.client.post('/api/tasks/', {'title': 'Test Task'})
        self.assertEqual(res.status_code, 201)
