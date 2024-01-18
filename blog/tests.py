from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from .models import BlogModel, UserModel

class BlogModelTests(APITestCase):
    
    def setUp(self):
        # Setup run before every test method.
        BlogModel.objects.create(title='Test Blog', description='Test Description')

    def test_blog_content(self):
        # Ensure blog is created correctly.
        blog = BlogModel.objects.get(title='Test Blog')
        self.assertEqual(blog.title, 'Test Blog')
        self.assertEqual(blog.description, 'Test Description')

class UserRegistrationTests(APITestCase):
    
    def test_create_user(self):
        # Ensure we can create a new user.
        url = reverse('user-register')
        data = {'email': 'test@redberry.ge', 'username': 'testuser'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class UserLoginTests(APITestCase):

    def setUp(self):
        # Setup run before every test method.
        self.user = UserModel.objects.create_user('test@redberry.ge', 'testpassword')
        self.url = reverse('login')

    def test_login_user(self):
        # Ensure we can login a user.
        data = {'email': 'test@redberry.ge', 'password': 'testpassword'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)
    
    def test_login_wrong_password(self):
        # Ensure user cannot login with wrong password.
        data = {'email': 'test@redberry.ge', 'password': 'wrong'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
