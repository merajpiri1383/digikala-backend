from rest_framework import serializers
from category.models import Category,SubCategory,Brand


class SubCategorySerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = SubCategory
        fields = ["id","name","image"]

class CategorySerializer(serializers.ModelSerializer) :
    class Meta :
        model = Category
        fields = ["id","name","image"]
    
    def to_representation(self,instance) : 
        context = super().to_representation(instance)
        context["sub_categories"] = SubCategorySerializer(instance=instance.sub_categorys,many=True).data
        return context

class BrandSerializer(serializers.ModelSerializer) : 
    class Meta :
        model = Brand
        fields = ["id","name","image"]