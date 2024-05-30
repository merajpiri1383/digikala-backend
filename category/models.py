from django.db import models

class BaseCategory(models.Model) : 
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="category_image")
    
    def __str__(self) : 
        return str(self.name)
    
    class Meta : 
        abstract = True
    

class Category(BaseCategory) : 
    pass 

class Brand(BaseCategory) : 
    pass 

class SubCategory(BaseCategory): 
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="sub_categorys")