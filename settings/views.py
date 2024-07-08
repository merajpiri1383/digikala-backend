from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from settings.models import Poster,Setting
from utils.permissions import IsStaffOrReadOnly
from settings.serializers import PosterSerializer

####################### Poster ############################



class PosterListCreateAPIView(APIView) : 

    permission_classes = [IsStaffOrReadOnly]
    serializer_class = PosterSerializer

    def dispatch(self,request) : 
        self.object,created = Setting.objects.get_or_create()
        return super().dispatch(request)

    def get(self,request) : 
        serializer = PosterSerializer(self.object.posters.all(),many=True,context={"request":request})
        return Response(serializer.data)
    
    def post(self,request) : 
        serializer = PosterSerializer(data=request.data)
        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

class PosterDestroyAPIView(APIView) : 
    permission_classes = [IsStaffOrReadOnly]
    serializer_class = PosterSerializer

    def delete(self,request,id) : 
        try : 
            poster = Poster.objects.get(id=id)
        except : 
            return Response({"detail":"poster with this id does not exist"},status.HTTP_400_BAD_REQUEST)
        poster.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


####################### Poster ############################