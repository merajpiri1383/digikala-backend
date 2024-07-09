from django.contrib import admin
from category.models import Brand,Category,SubCategory,PosterCategory

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(SubCategory) 
admin.site.register(PosterCategory)