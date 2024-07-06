from django.db import models
from product.models import Product

class BaseFeature(models.Model) : 
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=150)
    def __str__(self) : 
        return f"{self.name} : {self.value}"
    class Meta : 
        abstract = True

class Info(models.Model) : 
    name = models.CharField(max_length=150)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="info")

class SubInfo(BaseFeature) : 
    info = models.ForeignKey(Info,on_delete=models.CASCADE,related_name="sub_info")
    
class Feature(BaseFeature) : 
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="feature")