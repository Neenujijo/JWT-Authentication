from .models import User
# from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class RegisterTestCase(APITestCase):

    def test_register(self):
        data = {
            "username": "testcase",
            "email": "testcase@example.com",
            "phone_number": "+918921888036",
            "password": "NewPassword@123",
            
        }
        response = self.client.post(reverse('sign_up'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LoginTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testcase",
                                             email= "testcase@gmail.com",
                                             phone_number= "+918921888036",
                                             password="NewPassword@123")

    def test_login(self):
        data = {
            "username":"+918921888036",
            "password": "NewPassword@123"
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


