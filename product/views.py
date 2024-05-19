# rest framework tools
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
# permissions
from utils.permissions import IsStaffOrReadOnly,IsStaffOrNot
# serializers 
from product.serializers import ColorSerializer,ProductSerializer
# models 
from product.models import Color,Product
 
######################### color ##############################

class ColorBase :
    permission_classes = [IsStaffOrReadOnly]
    serializer_class = ColorSerializer 
    queryset = Color.objects.all()
 
class CreateColorAPIView(ColorBase,ListCreateAPIView) :
    pass

class ColorAPIView(ColorBase,RetrieveUpdateDestroyAPIView) :
    pass

######################### end color ##############################

######################### product ############################

class ProductBase: 
    permission_classes = [IsStaffOrReadOnly]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class CreateListProductAPIView(ProductBase,ListCreateAPIView): 
    pass 

class ProductAPIView(ProductBase,RetrieveUpdateDestroyAPIView) : 
    pass 

######################### end product ############################