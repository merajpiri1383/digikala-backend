from rest_framework.views import APIView
from user.serializers import UserSerializer
from utils.permissions import IsOwnUserOrNot
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class UserAPIView(APIView) : 
    permission_classes = [IsAuthenticated,IsOwnUserOrNot]
    
    def get(self,request) : 
        return Response(UserSerializer(request.user).data)