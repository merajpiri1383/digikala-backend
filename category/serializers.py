from rest_framework import serializers
from category.models import Category,SubCategory,Brand
from product.serializers import ProductSerializer


class SubCategorySerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = SubCategory
        fields = ["id","name","image","category"]
    
    def __init__(self,instance=None,**kwargs) :
        kwargs["partial"] = True
        super().__init__(instance,**kwargs)
    
    def to_representation(self,instance) : 
        context = super().to_representation(instance)
        context["category"] = {
            'id' : instance.category.id,
            'name' : instance.category.name
        }
        context["products"] = ProductSerializer(instance.products,many=True).data
        return context

class CategorySerializer(serializers.ModelSerializer) :
    class Meta :
        model = Category
        fields = ["id","name","image"]
        
    def __init__(self, instance=None, **kwargs):
        kwargs["partial"] = True
        super().__init__(instance,**kwargs)
        
    def to_representation(self,instance) : 
        context = super().to_representation(instance)
        context["sub_categories"] = SubCategorySerializer(instance=instance.sub_categorys,many=True).data
        return context

class BrandSerializer(serializers.ModelSerializer) : 
    class Meta :
        model = Brand
        fields = ["id","name","image"]