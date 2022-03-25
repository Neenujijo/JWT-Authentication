from urllib import response
from authentication.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

class ProfileTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testcase",
                                             email= "testcase@gmail.com",
                                             phone_number= "+918921888036",
                                             password="NewPassword@123")
        self.token=Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)



    def test_profile_create(self):
        data={
            "employee":"1",
            "first_name":"test",
            "last_name":"case",
            "employee_code":"0001",
            "employee_designation":"tester",
            "employee_department":"testing",
            "gender":"male",
        }
        response=self.client.post(reverse('profiles'),data)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)

    def test_profile_list(self):
        response=self.client.get(reverse('profiles'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)



