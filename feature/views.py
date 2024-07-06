from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils.permissions import IsStaffOrReadOnly
from feature.models import Feature,Info
from product.models import Product
from feature.serializers import InfoSerializer

########################## info #######################

class ListCreateInfoAPIView(APIView) : 
    permission_classes = [IsStaffOrReadOnly]
    serializer_class = InfoSerializer 

    def get_object(self,id) : 
        try : 
            self.object = Product.objects.get(id=id)
        except : 
            return Response(
                data={"detail":"product with this id does not exist"},
                status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,id) : 
        result = self.get_object(id)
        if result : return result
        serializer = InfoSerializer(self.object.info.all(),many=True)
        return Response(serializer.data)
    
    def post(self,request,id) : 
        if self.get_object(id) : return self.get_object
        data = request.data.copy()
        data["product"] = self.object.id
        serializer = InfoSerializer(data=data) 
        if serializer.is_valid() : 
            serializer.save() 
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else : 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class InfoAPIView(APIView) : 
    permission_classes = [IsStaffOrReadOnly]
    serializer_class = InfoSerializer

    def get_object(self,id,info_id) : 
        try : 
            self.product = Product.objects.get(id=id)
        except : 
            return Response(
                data={"detail":"product with this id does not exist"},
                status=status.HTTP_400_BAD_REQUEST)
        try : 
            self.info = self.product.info.get(id=info_id) 
        except : 
            return Response(
                data = {"detail" : "info with this id doens not exit"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def get(self,request,id,info_id)  :
        result = self.get_object(id,info_id) 
        if result :  return result
        serializer = InfoSerializer(self.info)
        return Response(serializer.data)
    
    def put(self,request,id,info_id) : 
        result = self.get_object(id,info_id) 
        if result : return result
        serializer = InfoSerializer(data=request.data , instance=self.info)
        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.data)
        else : 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id,info_id) : 
        result = self.get_object(id,info_id) 
        if result : return result
        self.info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

########################## end info #######################