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
from authentication.tasks import send_otp_code
# drf tools 
from drf_spectacular.utils import extend_schema,OpenApiParameter


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
        if not email : return Response({"detail":"email field is required ."},
                                       status=status.HTTP_400_BAS_REQUESt)
        if not otp : return Response({"detail":"otp field is required ."},
                                     status=status.HTTP_400_BAD_REQUEST)
        # check is email and otp is valid 
        try : 
            user = get_user_model().objects.get(email=email)
        except : 
            return Response({"detail":"ایمیل یا کد تایید اشتباهه"},
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
            return Response({"detail":"ایمیل یا کد تایید اشتباهه"},
                            status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView) :
    serializer_class = RegisterSerializer 
    throttle_scope = "login"
    
    @extend_schema(
        parameters = [
            OpenApiParameter(name="email",required=True),
        ]
    )
    
    def post(self,request) : 
        email = request.data.get("email")
        if not email : return Response({"detail":"email is required ."},
                                       status=status.HTTP_400_BAD_REQUEST)
        # check is email or password is valid 
        try : 
            user = get_user_model().objects.get(email=email)
        except : 
            user = get_user_model().objects.create(email=email)
        send_otp_code.apply_async(args=[user.email])
        return Response({"detail":"کد تایید ارسال شد ایمیل خود را بررسی کنید"})