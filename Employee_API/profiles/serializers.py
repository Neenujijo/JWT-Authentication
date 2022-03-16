from rest_framework import serializers
from .models import Profile



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


