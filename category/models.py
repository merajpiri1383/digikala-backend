from django.db import models
from django.utils.text import slugify

class BaseCategory(models.Model) : 
    name = models.CharField(max_length=300)
    
    def __str__(self) : 
        return str(self.name)
    
    @property
    def slug(self):
        return slugify(self.name,allow_unicode=True)
    
    class Meta : 
        abstract = True
    

class Category(BaseCategory) : 
    pass 

class Brand(BaseCategory) : 
    pass 