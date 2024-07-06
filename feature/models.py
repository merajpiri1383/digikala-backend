from django.db import models
from product.models import Product

class BaseFeature(models.Model) : 
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=150)
    def __str__(self) : 
        return f"{self.name} : {self.value}"
    class Meta : 
        abstract = True

class Info(BaseFeature) : 
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="info")
    
class Feature(BaseFeature) : 
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="feature")