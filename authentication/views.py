# rest framework tools 
from rest_framework.views import APIView 
from rest_framework import status 
from rest_framework.response import Response 
# serializers 
from user.serializers import UserSerializer
from authentication.serializers import RegisterSerializer 
# models 
from django.contrib.auth import get_user_model
# tasks 
from authentication.tasks import send_otp_code

class RegisterAPIView(APIView) : 
    def post(self,request) :
        serializer = RegisterSerializer(data=request.data) 
        if serializer.is_valid() : 
            user = serializer.save()
            send_otp_code.apply_async(args=[user.email])    
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else : 
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)