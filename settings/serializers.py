from rest_framework import serializers
from settings.models import Poster,Setting

class PosterSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Poster
        fields = ["id","image"]
    
    def create(self,validated_data):
        validated_data["setting"] = Setting.objects.get_or_create()[0]
        return super().create(validated_data)
    

class SettingSerializer(serializers.ModelSerializer) :
    image = PosterSerializer() 
    class Meta : 
        model = Setting 
        fields = ["id","posters"]
    