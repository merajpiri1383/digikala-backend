# rest framework tools 
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.permissions import IsAuthenticated
# models 
from cart.models import Cart,CartProduct
from product.models import Product
# serializers 
from cart.serializers import CartSerializer,CartProductSerializer

class CartProductAPIView(APIView) : 
    permission_classes = [IsAuthenticated]
    
    def get_cart(self,request) : 
        if not request.data.get("id") : 
            return Response({"detail":"id is required"},status=status.HTTP_400_BAD_REQUEST)
        try : 
            self.product = Product.objects.get(id=request.data.get("id"))
        except : 
            return Response({"detail":"product with this id does not exist"},status=status.HTTP_400_BAD_REQUEST)
        try : 
            self.cart = request.user.carts.all().get(is_paid=False)
        except : 
            self.cart = Cart.objects.create(user=self.request.user)
        try : 
            self.cart_product = self.cart.cart_products.get(product=self.product)
        except : 
            self.cart_product = CartProduct.objects.create(cart=self.cart,product=self.product)
    
    def get(self,request) : 
        search = self.get_cart(request)
        if search : return search 
        serializer = CartSerializer(self.cart)
        return Response(serializer.data)
    
    def delete(self,request) : 
        search = self.get_cart(request)
        if search : return search 
        if self.cart_product.count > 1 : 
            self.cart_product.count -= 1
            self.cart_product.save()
        elif self.cart_product.count == 1 or self.cart_product.count == 0 : 
            self.cart_product.delete()
        serializer = CartSerializer(self.cart)
        return Response(serializer.data)
    
    def post(self,request):
        search = self.get_cart(request)
        if search : return search 
        self.cart_product.count += 1
        self.cart_product.save()
        serializer = CartSerializer(self.cart)
        return Response(serializer.data,status=status.HTTP_201_CREATED) 