from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError
from tasks.models import Task,CustomUser
from tasks.serializers import TaskSerializer,UserSerializer

User = get_user_model()

# Authentication testing
class Auth(APITestCase):
    def test_register_user(self):
        url = reverse('register')  # Ensure this matches the URL pattern for RegisterView
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'securepassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'User created successfully')

    def test_login_user(self):
        User.objects.create_user(username='testuser', password='securepassword')
        url = reverse('login')  # Ensure this matches the URL pattern for LoginView
        data = {
            'username': 'testuser',
            'password': 'securepassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)


# Task CRUD testing
class Task(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='securepassword')
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        self.task_url = reverse('task-list-create')  # Ensure this matches the URL pattern for TaskCreateView

    def test_create_task(self):
        data = {
            'title': 'New Task',
            'status': 'pending'
        }
        response = self.client.post(self.task_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Task')

    def test_update_task(self):
        task = Task.objects.create(title='Old Task', status='pending', user=self.user)
        url = reverse('task-detail', args=[task.id])  # Ensure this matches the URL pattern for TaskUpdateView
        data = {'title': 'Updated Task', 'status': 'completed'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Task')
        self.assertEqual(response.data['status'], 'completed')

# User Serializer conversion testing
class UserSerializers(APITestCase):
    def test_valid_user_serializer(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'securepassword'
        }
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('securepassword'))

    def test_invalid_user_serializer(self):
        data = {
            'username': 'testuser',
            'password': 'securepassword'
        }
        serializer = UserSerializer(data=data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
