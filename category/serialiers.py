from rest_framework import serializers
from category.models import Category,Brand

class CategorySerializer(serializers.ModelSerializer) :
    class Meta :
        model = Category
        fields = "__all__"

class BrandSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Brand
        fields = "__all__"