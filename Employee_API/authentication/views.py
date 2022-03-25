from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
# from rest_framework_simplejwt.tokens import RefreshToken

from profiles.models import User
from . import serializers
from . import models
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

# from rest_framework.decorators import api_view
# User=get_user_model

class UserLogoutView(generics.GenericAPIView):

    def post(self,request):

        if request.method == 'POST':
            request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class UserView(generics.GenericAPIView):
    queryset =User.objects.all()
    serializer_class=serializers.UserCreationSerializer

    @swagger_auto_schema(operation_summary="Get all Employee")
    def get(self,request):

        emp=User.objects.all()
        serializer=self.serializer_class(instance=emp,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    
class UserEditView(generics.GenericAPIView):
    queryset =User.objects.all()
    serializer_class=serializers.UserCreationSerializer

    def get(self,request,user_id):

        user=get_object_or_404(User,pk=user_id)

        serializer=self.serializer_class(instance=user)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put(self,request,user_id):
        data=request.data

        user=get_object_or_404(User,pk=user_id)

        serializer=self.serializer_class(data=data,instance=user)


        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,user_id):

        user=get_object_or_404(User,pk=user_id)

        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)




class UserCreateView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class=serializers.UserCreationSerializer


    @swagger_auto_schema(operation_summary="Create a user account by signing Up")
    def post(self,request):

        serializer=self.serializer_class(data=request.data)

        data = {}

        if serializer.is_valid():
            user=serializer.save()

            data['response'] = "Registration Successful!"
            data['username'] = user.username
            data['email'] = user.email

            
            # refresh = RefreshToken.for_user(account)
            # data['token'] = {
            #                     'refresh': str(refresh),
            #                     'access': str(refresh.access_token),
            #                 }
        else:
            data=serializer.errors

        return Response(data,status=status.HTTP_201_CREATED)
        
        

    


        
        

            