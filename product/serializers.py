from rest_framework import serializers 
from product.models import Product,Color

class ColorSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Color 
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Product 
        fields = ["name","price","discount","category","brand","picture","introduction"]