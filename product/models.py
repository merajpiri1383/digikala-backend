from django.db import models
from category.models import SubCategory,Brand
from django.utils.text import slugify


class Color(models.Model) : 
    name = models.CharField(max_length=150)
    hex = models.SlugField()
    def __str__(self) : 
        return str(self.name)

class Product(models.Model) : 
    name = models.CharField(max_length=300)
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(default=0)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name="products",null=True,blank=True)
    sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE,related_name="products")
    colors = models.ManyToManyField(Color,related_name="colors")
    picture = models.ImageField(upload_to="products/pictures")
    introduction = models.TextField(null=True,blank=True)
    sell_count = models.PositiveIntegerField(default=0)
    
    @property 
    def slug(self) : 
        return slugify(self.name,allow_unicode=True)
    
class Image(models.Model) : 
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="images")
    picture = models.ImageField(upload_to="products/pictures")