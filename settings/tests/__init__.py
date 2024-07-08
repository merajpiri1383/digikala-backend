from rest_framework.test import APITestCase
from settings.models import Setting,Poster
from django.core.files.uploadedfile import SimpleUploadedFile
from pathlib import Path
from django.contrib.auth import get_user_model

class BaseSettingCase (APITestCase) : 

    @classmethod
    def setUpTestData(self) : 
        self.image_path = Path(__file__).parent.parent.parent /"static/test.jpg"
        self.settings = Setting.objects.create()
        self.poster_1 = Poster.objects.create(
            setting = self.settings,
            image = SimpleUploadedFile(
                name= "poster_1",
                content=  open(self.image_path,"rb").read(),
                content_type="image/jpg"
            )
        )
        self.user = get_user_model().objects.create(email="test@gmail.com")
        self.staff_user = get_user_model().objects.create(email="test_staff@gmail.com",is_staff=True)
        self.data = {
            "setting" : self.settings.id,
            "image" : SimpleUploadedFile(
                name="poster_2.jpg",
                content= open(self.image_path,"rb").read(),
                content_type="image/jpg"
            )
        }
        super().setUpTestData()
