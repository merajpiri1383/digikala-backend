from rest_framework import serializers
from django.contrib.auth import get_user_model
import re 

password_regex = re.compile(r"(?=.*[0-9])(?=.*[a-z]).{8,16}")


class RegisterSerializer(serializers.ModelSerializer) : 
    password = serializers.SlugField()
    class Meta : 
        model = get_user_model() 
        fields = ["email","password"]
    
    def validate(self,data):
        if not password_regex.findall(data.get("password")) : 
            raise serializers.ValidationError("password must contains letters and integers and at least 8 character ")
        return data
    
    def create(self,data): 
        print("create new user")
        user = get_user_model().objects.create(email=data.get("email")) 
        user.set_password(data.get("password"))
        user.save()
        return user