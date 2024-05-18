from rest_framework import serializers 
from django.contrib.auth import get_user_model 

class UserSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = get_user_model() 
        fields = ["email","is_active","is_staff","is_manager"]
        
    def to_representation(self,instance) : 
        context = super().to_representation(instance)
        context["joind_date"] = instance.joind.strftime("%Y-%m-%d")
        context["joind_time"] = instance.joind.strftime("%H:%M-%S")
        return context