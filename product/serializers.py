from rest_framework import serializers 
from product.models import Product,Color,Image
from category.models import SubCategory


class ImageSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Image 
        fields = ["id","picture","product"]

class ColorSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Color 
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = Product 
        fields = ["id","name","price","discount","sub_category","brand","picture","introduction"]

    def __init__(self,instnace=None,**kwargs) : 
        if instnace : 
            kwargs["partial"] = True
        super().__init__(instance=instnace,**kwargs)
    
    def to_representation(self,instance) :  
        context = super().to_representation(instance)
        context["sub_category"] = {
            "id" : instance.sub_category.id,
            "name" : instance.sub_category.name,
        }
        context["images"] = ImageSerializer(
            instance.images,
            many=True,
            context={"request" : self.context.get("request")}
            ).data
        return context