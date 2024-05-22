# rest framework tools 
from rest_framework.views import APIView 
from rest_framework import status 
from rest_framework.response import Response 
# serializers 
from user.serializers import UserSerializer
from authentication.serializers import AuthUserSerializer,ChangePasswordSerializer
# models 
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
# tasks 
from authentication.tasks import send_otp_code
# drf tools 
from drf_spectacular.utils import extend_schema,OpenApiParameter
# permissions 
from rest_framework.permissions import IsAuthenticated 


# activate email 

class ActivateEmailAPIView(APIView) : 
    serializer_class = UserSerializer
    throttle_scope = "login"
    @extend_schema(
        parameters = [
            OpenApiParameter(name="email",required=True),
            OpenApiParameter(name="otp",required=True,description="code to activate account .")
        ]
    )
    def post(self,request) : 
        email = request.data.get("email")
        otp = request.data.get("otp")
        if not email : return Response({"detail":"required-email"},
                                       status=status.HTTP_400_BAD_REQUEST)
        if not otp : return Response({"detail":"required-otp"},
                                     status=status.HTTP_400_BAD_REQUEST)
        # check is email and otp is valid 
        try : 
            user = get_user_model().objects.get(email=email)
        except : 
            return Response({"detail":"wrong-email-otp"},
                            status=status.HTTP_400_BAD_REQUEST)
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
            return Response({"detail":"wrong-email-otp"},
                            status=status.HTTP_400_BAD_REQUEST)

class AuthAPIView(APIView) :
    serializer_class = AuthUserSerializer 
    throttle_scope = "login"
    
    @extend_schema(
        parameters = [
            OpenApiParameter(name="email",required=True),
        ]
    )
    
    def post(self,request) : 
        email = request.data.get("email")
        if not email : return Response({"detail":"required-email"},
                                       status=status.HTTP_400_BAD_REQUEST)
        # check is email or password is valid 
        user,created = get_user_model().objects.get_or_create(email=email)
        send_otp_code.apply_async(args=[user.email])
        return Response({"created":created})

# change password 
class ChangePasswordAPIView(APIView) : 
    permission_classes = [IsAuthenticated]
    def put(self,request) : 
        serializer = ChangePasswordSerializer(instance=request.user,data=request.data)
        if serializer.is_valid() : 
            serializer.save() 
            return Response(data=serializer.data)
        else : 
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST) 


# login with password for registered users 
class LoginAPIView(APIView) : 
    serializer_class = UserSerializer
    def post(self,request) : 
        if not request.data.get("email") : 
            return Response(data={"detail" : "required-email"},
                            status=status.HTTP_400_BAD_REQUEST)
        try : 
            user = get_user_model().objects.get(email=request.data.get("email"))
        except : 
            return Response(data={"detail":"invalid-email"},
                            status=status.HTTP_400_BAD_REQUEST)
        if not request.data.get("password") : 
            return Response(data={"detail" : "required-password"},
                            status=status.HTTP_400_BAD_REQUEST)
        if user.check_password(request.data.get("password")) : 
            data = {}
            data["user"] = UserSerializer(user).data
            refresh_token = RefreshToken.for_user(user)
            data["access_token"] = str(refresh_token.access_token)
            data["refresh_token"] = str(refresh_token)
            return Response(data)
        else : 
            return Response(data={"detail":"invalid-password"},
                            status=status.HTTP_400_BAD_REQUEST)