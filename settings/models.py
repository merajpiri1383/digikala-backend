from django.db import models

class Setting(models.Model) : 
    pass 

class Poster(models.Model) : 
    setting = models.ForeignKey(Setting,on_delete=models.CASCADE,related_name="posters")
    image = models.ImageField(upload_to="setting/posters")

    def __str__(self) : 
        return f"Poster {self.image}"