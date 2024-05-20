from rest_framework import serializers 
from cart.models import Cart,CartProduct
from user.serializers import UserSerializer

class CartProductSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = CartProduct 
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Cart
        fields = ["id","is_paid"]
    
    def to_representation(self, instance):
        context = super().to_representation(instance)
        context["create_date"] = instance.created.strftime("%Y-%m-%d")
        context["create_time"] = instance.created.strftime("%H:%M:%S")
        context["user"] = UserSerializer(instance.user).data
        context["cart_products"] = CartProductSerializer(instance.cart_products.all(),many=True).data
        return context
    