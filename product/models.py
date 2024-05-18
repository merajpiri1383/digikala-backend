from django.db import models
from category.models import Category,Brand


class Color(models.Model) : 
    name = models.CharField(max_length=150)
    hex = models.SlugField()
    def __str__(self) : 
        return str(self.name)

class Image(models.Model) : 
    picture = models.ImageField(upload_to="products/pictures")

class Product(models.Model) : 
    name = models.CharField(max_length=300)
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(default=0)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name="products",null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,name="products",null=True,blank=True)
    colors = models.ManyToManyField(Color)
    picture = models.ImageField(upload_to="products/pictures")
    images = models.ManyToManyField(Image)
    introduction = models.TextField(null=True,blank=True)
    
class BaseProperty(models.Model) : 
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=150)
    def __str__(self) : 
        return f"{self.name} : {self.value}"
    class Meta : 
        abstract = True

class Property(BaseProperty) : 
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="properties")
    
class Feature(BaseProperty) : 
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="features")