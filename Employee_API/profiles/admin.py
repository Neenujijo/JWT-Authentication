from django.contrib import admin
from .models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['first_name','employee_code','employee_designation']
    list_filter=['employee_designation']
    