from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils.permissions import IsStaffOrReadOnly
from feature.models import Feature,Info
from product.models import Product
from feature.serializers import FeatureSerializer,InfoSerializer

########################## feature #######################

class ListCreateFeatureAPIView(APIView) : 
    permission_classes = [IsStaffOrReadOnly]
    serializer_class = FeatureSerializer 

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
        serializer = FeatureSerializer(self.object.feature.all(),many=True)
        return Response(serializer.data)
    
    def post(self,request,id) : 
        if self.get_object(id) : return self.get_object
        data = request.data.copy()
        data["product"] = self.object.id
        serializer = FeatureSerializer(data=data) 
        if serializer.is_valid() : 
            serializer.save() 
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else : 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class FeatureAPIView(APIView) : 
    permission_classes = [IsStaffOrReadOnly]
    serializer_class = FeatureSerializer 

    def get_object(self,id,feature_id) : 
        try : 
            self.product = Product.objects.get(id=id)
        except : 
            return Response(
                data={"detail":"product with this id does not exist"},
                status=status.HTTP_400_BAD_REQUEST)
        try : 
            self.feature = self.product.feature.get(id=feature_id) 
        except : 
            return Response(
                data = {"detail" : "feature with this id doens not exit"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def get(self,request,id,feature_id)  :
        result = self.get_object(id,feature_id) 
        if result :  return result
        serializer = FeatureSerializer(self.feature)
        return Response(serializer.data)
    
    def put(self,request,id,feature_id) : 
        result = self.get_object(id,feature_id) 
        if result : return result
        serializer = FeatureSerializer(data=request.data , instance=self.feature)
        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.data)
        else : 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id,feature_id) : 
        result = self.get_object(id,feature_id) 
        if result : return result
        self.feature.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

########################## end feature #######################

########################## info ##############################

class ListCreateInfoAPIView(APIView) : 
    
    permission_classes = [IsStaffOrReadOnly]
    serializer_classe = InfoSerializer

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
        result = self.get_object(id)
        if result : return result 
        data = request.data.copy()
        data["product"] = self.object.id
        serializer = InfoSerializer(data=data)
        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else : 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

########################## end info ##########################