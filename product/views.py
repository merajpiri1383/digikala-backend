# rest framework tools
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# permissions
from utils.permissions import IsStaffOrReadOnly
# serializers 
from product.serializers import ColorSerializer,ProductSerializer,ImageSerializer
# models 
from product.models import Color,Product
from category.models import Category
 
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

class ImageProductAPIView(APIView) : 
    permission_classes = [IsStaffOrReadOnly] 
    serializer_class = ProductSerializer

    def get_product(self,pk) :
        try : 
            self.product = Product.objects.get(id=pk)
        except : 
            return Response({"detail":"object does not exist ."},status=status.HTTP_400_BAD_REQUEST)

    def post(self,request,pk) : 
        if self.get_product(pk) : return self.get_product(pk)
        if self.product.images.count() == 4 : return Response(
            {"detail" : "the product have 4 image "},
            status= status.HTTP_400_BAD_REQUEST
        )
        data = request.data.copy()
        data["product"] = self.product.id
        serializer = ImageSerializer(data=data)
        if serializer.is_valid() : 
            serializer.save() 
            return Response(ProductSerializer(self.product).data)
        else : 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,image_id) :
        if self.get_product(pk) : return self.get_product(pk)
        image = self.product.images.filter(id=image_id)
        if image : 
            image.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else : 
            return Response( 
                data = {"detail":"image with this id does not exist"} , 
                status = status.HTTP_400_BAD_REQUEST
            )
######################### end product ############################ 


######################### most sell product ###################### 

class MostSellProductAPIView(ListAPIView) : 
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by("-sell_count")

class MostSellCategoryAPIView(APIView) : 
    serializer_class = ProductAPIView

    def get(self,request,id) : 
        try : 
            category = Category.objects.get(id=id)
        except : 
            return Response({"detail":"category with this id does not exist"},status.HTTP_400_BAD_REQUEST)
        products = []
        for sub_category in category.sub_categorys.all() :
            for product in sub_category.products.all().order_by("-sell_count") : 
                products.append(product)
        return Response(ProductSerializer(products,many=True,context={"request":request}).data)