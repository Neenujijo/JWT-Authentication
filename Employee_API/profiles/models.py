from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()
# Create your models here.

class Profile(models.Model):

    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100,null=True, blank=True)
    last_name=models.CharField(max_length=100,null=True, blank=True)
    employee_code=models.CharField(max_length=300, null=True, blank=True)
    employee_designation=models.CharField(max_length=100,null=True, blank=True)
    employee_department=models.CharField(max_length=50,null=True, blank=True)
    gender=models.CharField(max_length=10,null=True, blank=True)


    def __str__(self):
        return f"<Profile {self.first_name} by {self.employee}>"


    
    
