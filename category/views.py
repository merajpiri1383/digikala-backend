# rest framework tools
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
# serializers
from category.serializers import CategorySerializer,BrandSerializer,SubCategorySerializer
# permissions
from utils.permissions import IsStaffOrReadOnly
# models 
from category.models import Category,Brand,SubCategory

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

class BaseSubCategory(CategoryBase): 
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()
    permission_classes = [IsStaffOrReadOnly]
    
class ListCreateSubCategoryAPIView(BaseSubCategory,ListCreateAPIView) : 
    pass 

class SubCategoryAPIView(BaseSubCategory,APIView) : 
    
    def get_object(self,pk) : 
        try : 
            self.object = SubCategory.objects.get(id=pk)
        except : 
            return Response({"not-found"},status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,pk) : 
        if self.get_object(pk) : return self.get_object(pk)
        return Response(SubCategorySerializer(self.object,context={"request":request}).data)
    
    def put(self,request,pk) : 
        if self.get_object(pk) : return self.get_object(pk) 
        serializer = SubCategorySerializer(self.object,data=request.data,partial=True,context={"request":request})
        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.data)
        else : 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk) : 
        if self.get_object(pk) : return self.get_object(pk) 
        self.object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)