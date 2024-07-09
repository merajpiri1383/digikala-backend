# rest framework tools
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from category.serializers import CategorySerializer,BrandSerializer,SubCategorySerializer,PosterCategorySerializer
from utils.permissions import IsStaffOrReadOnly
from category.models import Category,Brand,SubCategory,PosterCategory

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

class CreateListBrandAPIView(BrandBase,ListCreateAPIView) :
    pass

class BrandAPIView(BrandBase,RetrieveUpdateDestroyAPIView) :
    pass

class BaseSubCategory: 
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()
    permission_classes = [IsStaffOrReadOnly]
    
class ListCreateSubCategoryAPIView(BaseSubCategory,ListCreateAPIView) : 
    pass 

class SubCategoryAPIView(BaseSubCategory,RetrieveUpdateDestroyAPIView) : 
    pass 

#################### Poster Category ########################

class PosterCategoryCreateListAPIView(APIView) : 

    permission_classes = [IsStaffOrReadOnly]
    serializer_class = None 

    def dispatch(self,request,id) : 
        self.result = None 
        try : 
            self.object = Category.objects.get(id=id)
        except : 
            self.result = Response({"detail":"category with this id does not exist "},status.HTTP_400_BAD_REQUEST)
        return super().dispatch(request,id)

    def get(self,request,id) : 
        if self.result : return self.result
        serializer = PosterCategorySerializer(self.object.posters.all(),many=True,context={"request":request})
        return Response(serializer.data)
    
    def post(self,request,id) : 
        if self.result : return self.result
        data = request.data.copy()
        data["category"] = id
        serializer = PosterCategorySerializer(data=data)
        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

class PosterCategoryDetailAPIView(DestroyAPIView) : 
    permission_classes = [IsStaffOrReadOnly]
    serializer_class = PosterCategorySerializer
    queryset = PosterCategory.objects.all()