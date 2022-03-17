from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from profiles.models import User
from . import serializers


# Create your views here.


class UserView(generics.GenericAPIView):
    # queryset =User.objects.all()
    serializer_class=serializers.UserCreationSerializer

    @swagger_auto_schema(operation_summary="Get all Employee")
    def get(self,request):

        emp=User.objects.all()
        serializer=self.serializer_class(instance=emp,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)



class UserCreateView(generics.GenericAPIView):

    serializer_class=serializers.UserCreationSerializer


    @swagger_auto_schema(operation_summary="Create a user account by signing Up")
    def post(self,request):
        data=request.data

        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    

