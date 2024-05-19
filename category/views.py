# rest framework tools
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# serializers
from category.serialiers import CategorySerializer
# permissions
from utils.permissions import IsStaffOrNot
# models 
from category.models import Category,Brand

class CategoryBase :
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrNot]
    queryset = Category.objects.all()

class BrandBase :
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrNot]
    queryset = Brand.objects.all()

class CreateListCategoryAPIView(CategoryBase,ListCreateAPIView) :
    pass

class CategoryAPIView(CategoryBase,RetrieveUpdateDestroyAPIView) :
    pass

class CreateListBrandAPIView(CategoryBase,ListCreateAPIView) :
    pass

class BrandAPIView(BrandBase,RetrieveUpdateDestroyAPIView) :
    pass