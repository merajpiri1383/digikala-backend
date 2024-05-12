from rest_framework import serializers 
from django.contrib.auth import get_user_model 

class UserSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = get_user_model() 
        fields = ["email"]
    
    
    def validate(self,data): 
        print("validation of data")
        return data
    
    def create(self,validated_data): 
        print('create new object of user ')
        return get_user_model().objects.get(email="test1@gmail.com")