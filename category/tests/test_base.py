from rest_framework.test import APITestCase
from pathlib import Path
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile


class TestBase(APITestCase) :
    @classmethod
    def setUpTestData(self) :
        self.image = Path(__file__).parent.parent.parent / "static/test.jpg"
        self.data = {
            'name' : 'item 1',
            'image' : SimpleUploadedFile(
                name= "test.jpg",
                content=open(self.image,"rb").read(),
                content_type="image/jpg"
            )
        }
        self.data_2 = {
            'name' : 'item 2',
            'image' : SimpleUploadedFile(
                name = "test2.jpg",
                content=open(self.image,"rb").read(),
                content_type="image/jpg"
            )
        }
        self.user = get_user_model().objects.create(email="test@gmail.com")
        self.staff_user = get_user_model().objects.create(email="staff@gmail.com", is_staff=True)