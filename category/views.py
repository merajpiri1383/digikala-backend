# rest framework tools
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# serializers
from category.serializers import CategorySerializer,BrandSerializer
# permissions
from utils.permissions import IsStaffOrReadOnly
# models 
from category.models import Category,Brand

class CategoryBase :
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly]
    queryset = Category.objects.all()

class BrandBase :
    serializer_class = BrandSerializer
    permission_classes = [IsStaffOrReadOnly]
    queryset = Brand.objects.all()

class CreateListCategoryAPIView(CategoryBase,ListCreateAPIView) :
    pass

class CategoryAPIView(CategoryBase,RetrieveUpdateDestroyAPIView) :
    pass

class CreateListBrandAPIView(CategoryBase,ListCreateAPIView) :
    pass

class BrandAPIView(BrandBase,RetrieveUpdateDestroyAPIView) :
    pass