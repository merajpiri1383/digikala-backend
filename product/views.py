# rest framework tools
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
# permissions
from category.permissions import IsStaffOrReadOnly
# serializers 
from product.serializers import ColorSerializer
# models 
from product.models import Color
 

class ColorBase :
    permission_classes = [IsStaffOrReadOnly]
    serializer_class = ColorSerializer 
    queryset = Color.objects.all()

class CreateColorAPIView(ColorBase,ListCreateAPIView) :
    pass

class ColorAPIView(ColorBase,RetrieveUpdateDestroyAPIView) :
    pass