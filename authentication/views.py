# rest framework tools 
from rest_framework.views import APIView 
from rest_framework import status 
from rest_framework.response import Response 
from rest_framework.decorators import api_view
# serializers 
from user.serializers import UserSerializer
from authentication.serializers import RegisterSerializer 
# models 
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
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
    
# activate email 

@api_view(["post"])
def activate_email_api_view(request) : 
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