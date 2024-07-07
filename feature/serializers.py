from rest_framework import serializers 
from feature.models import Feature,Info,SubInfo

class FeatureSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Feature
        fields = ["id","product","name","value"]
    
    def __init__(self,instance=None,**kwargs) : 
        if instance : 
            kwargs["partial"] = True
        return super().__init__(instance,**kwargs)
    
    def to_representation(self,instnace) :  
        context = super().to_representation(instnace)
        context["product"] = {
            "id" : instnace.product.id,
            "name" :instnace.product.name,
        }
        return context

class SubInfoSerializer(serializers.ModelSerializer) :

    def __init__(self,instance=None,**kwargs) : 
        if instance : 
            kwargs["partial"] = True 
        super().__init__(instance,**kwargs)
         
    class Meta : 
        model = SubInfo
        fields = ["id","info","name","value"]

class InfoSerializer(serializers.ModelSerializer) : 

    def __init__(self,instance=None,**kwargs) : 
        if instance : 
            kwargs["partial"] = True
        super().__init__(instance,**kwargs)
 
    class Meta : 
        model = Info
        fields = ["id","product","name"]
    
    def to_representation(self,instance) : 
        context = super().to_representation(instance)
        context["sub_info"] = SubInfoSerializer(instance.sub_info.all(),many=True).data
        return context