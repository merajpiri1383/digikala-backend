from rest_framework import serializers 
from product.models import Product,Color

class ColorSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Color 
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Product 
        fields = ["name","price","discount","sub_category","brand","picture","introduction"]
    
    def to_representation(self,instance) : 
        context = super().to_representation(instance)
        context["sub_category"] = {
            "id" : instance.sub_category.id,
            "name" : instance.sub_category.name,
        }
        return context