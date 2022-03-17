from django.shortcuts import render,get_object_or_404
from rest_framework import generics,status
from rest_framework.response import Response
from . import serializers
from .models import Profile
from authentication.permissions import AdminOrReadOnly
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import AuthenticationFailed

User=get_user_model()

# Create your views here.

# class HelloProfileView(generics.GenericAPIView):
#     def get(self,request):
#         return Response(data={"message":"Hello employee"},status=status.HTTP_200_OK)



class ProfileCreateView(generics.GenericAPIView):
    queryset =Profile.objects.all()
    serializer_class=serializers.ProfileCreationSerializer
    permission_classes=[AdminOrReadOnly]

    @swagger_auto_schema(operation_summary="Get all Employee profiles")
    def get(self,request):

        profiles=Profile.objects.all()
        serializer=self.serializer_class(instance=profiles,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Create an Employee Profile")
    def post(self,request):
        data=request.data

        serializer=self.serializer_class(data=data)

        user=request.user

        if serializer.is_valid():
            serializer.save(employee=user)

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ProfileIdView(generics.GenericAPIView):
    serializer_class=serializers.ProfileCreationSerializer
    permission_classes=[AdminOrReadOnly]


    @swagger_auto_schema(operation_summary="View the detail of profile by its ID")
    def get(self,request,profile_id):
        
        profile=get_object_or_404(Profile,pk=profile_id)

        serializer=self.serializer_class(instance=profile)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Update an profile by its ID")
    def put(self,request,profile_id):
        data=request.data

        profile=get_object_or_404(Profile,pk=profile_id)

        serializer=self.serializer_class(data=data,instance=profile)


        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary="Delete profile by its ID")
    def delete(self,request,profile_id):

        profile=get_object_or_404(Profile,pk=profile_id)

        profile.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)




# class UserLoginView(generics.GenericAPIView):

#     serializer_class=serializers.UserSerializer

#     def post(self,request):
#         phone_number=request.data.get('phone_number')
#         password=request.data.get('password')

#         user = User.objects.filter(phone_number=phone_number).first()

#         if user is None:
#             raise AuthenticationFailed('User not found!')

#         if not user.check_password(password):
#             raise AuthenticationFailed('Incorrect password!')

        

