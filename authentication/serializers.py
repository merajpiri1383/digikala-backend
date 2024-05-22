from rest_framework import serializers
from django.contrib.auth import get_user_model
import re 

password_regex = re.compile(r"(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z]).{8,16}")

class AuthUserSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = get_user_model() 
        fields = ["email"]

    
class ChangePasswordSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = get_user_model()
        fields = ["password"]
    def update(self,instance,validated_data) : 
        instance.set_password(validated_data.get("password"))
        instance.save()
        return instance
    
    def validate(self,data) : 
        if not password_regex.findall(data.get("password")) : 
            raise serializers.ValidationError("weak-password")
        return data