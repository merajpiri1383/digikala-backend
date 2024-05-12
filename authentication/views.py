# rest framework tools 
from rest_framework.views import APIView 
from rest_framework import status 
from rest_framework.response import Response 
# serializers 
from user.serializers import UserSerializer
from authentication.serializers import RegisterSerializer ,ChangePasswordSerializer
# models 
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
# tasks 
from authentication.tasks import send_otp_code,forget_password
# drf tools 
from drf_spectacular.utils import extend_schema, OpenApiExample,OpenApiParameter
# permissions 
from rest_framework.permissions import IsAuthenticated


class RegisterAPIView(APIView) :
    serializer_class = RegisterSerializer
    
    @extend_schema(
        parameters = [
            OpenApiParameter(name="email",required=True), 
            OpenApiParameter(name="password",required=True,description="contains a least 8 chatacter and integer")
        ]
    )
    def post(self,request) :
        serializer = RegisterSerializer(data=request.data) 
        if serializer.is_valid() : 
            user = serializer.save()
            send_otp_code.apply_async(args=[user.email])    
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else : 
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# activate email 

class ActivateEmailAPIView(APIView) : 
    serializer_class = UserSerializer
    @extend_schema(
        parameters = [
            OpenApiParameter(name="email",required=True),
            OpenApiParameter(name="otp",required=True,description="code to activate account .")
        ]
    )
    def post(self,request) : 
        email = request.data.get("email")
        otp = request.data.get("otp")
        if not email : return Response({"detail":"email field is required ."},status=status.HTTP_400_BAS_REQUESt)
        if not otp : return Response({"detail":"otp field is required ."},status=status.HTTP_400_BAD_REQUEST)
        # check is email and otp is valid 
        try : 
            user = get_user_model().objects.get(email=email)
        except : 
            return Response({"detail":"email or otp is not valid"},status=status.HTTP_400_BAD_REQUEST)
        if str(user.otp) == otp : 
            user.is_active = True 
            user.save()
            data = {}
            data["user"] = UserSerializer(user).data
            refresh_token = RefreshToken.for_user(user)
            data["refresh_token"] = str(refresh_token)
            data["access_token"] = str(refresh_token.access_token)
            return Response(data=data) 
        else : 
            return Response({"detail":"email or otp is not valid"},status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView) :
    serializer_class = RegisterSerializer 
    
    @extend_schema(
        parameters = [
            OpenApiParameter(name="email",required=True),
            OpenApiParameter(name="password",required=True),
        ]
    )
    
    def post(self,request) : 
        email = request.data.get("email")
        password = request.data.get("password")
        if not email : return Response({"detail":"email is required ."},status=status.HTTP_400_BAD_REQUEST)
        if not password : return Response({"detail":"password is required ."},status=status.HTTP_400_BAD_REQUEST)
        # check is email or password is valid 
        try : 
            user = get_user_model().objects.get(email=email)
        except : 
            return Response({"detail":"email or password is not corrent"},status=status.HTTP_400_BAD_REQUEST)
        if user.check_password(password) : 
            refresh_token = RefreshToken.for_user(user)
            data = {}
            data["user"] = UserSerializer(user).data
            data["access_token"] = str(refresh_token.access_token)
            data["refresh_token"] = str(refresh_token)
            return Response(data=data)
        else : 
            return Response({"detail":"email or password is not corrent"},status=status.HTTP_400_BAD_REQUEST)
    
class ForgetPasswordAPIView(APIView) : 
    serializer_class = RegisterSerializer
    
    @extend_schema(
        parameters = [
            OpenApiParameter(name="email",required=True)
        ]
    )
    def post(self,request) : 
        email = request.data.get("email")
        if not email : return Response({"detail":"email field is required ."},status=status.HTTP_400_BAD_REQUEST)
        forget_password.apply_async(args=[email])
        return Response({"detail":"code is sent to you "})


class ResetPasswordAPIView(APIView) : 
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    @extend_schema(
        parameters = [
            OpenApiParameter(name="password",required=True)
        ]
    )
    def put(self,request) : 
        data =  request.data.copy()
        data["email"] = request.user.email
        serializer = ChangePasswordSerializer(data=data,instance=request.user)
        if serializer.is_valid(): 
            serializer.save()
            return Response(data={"detail":"your password has been changed successfully ."})
        else : 
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)