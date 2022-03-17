from rest_framework import serializers
from .models import Profile
from phonenumber_field.serializerfields import PhoneNumberField
from django.contrib.auth import get_user_model

User=get_user_model



class ProfileCreationSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField(max_length=100)
    last_name=serializers.CharField(max_length=100)
    employee_code=serializers.CharField(max_length=300)
    employee_designation=serializers.CharField(max_length=100)
    employee_department=serializers.CharField(max_length=50)
    gender=serializers.CharField(max_length=10)


    class Meta:
        model=Profile
        fields=['id','employee','first_name','last_name','employee_code',
        'employee_designation','employee_department','gender',
        ]


class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(min_length=8,write_only=True)


    class Meta:
        model=User
        fields=['phone_number','password']

