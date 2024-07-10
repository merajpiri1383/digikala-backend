from rest_framework.test import APITestCase
from pathlib import Path
from category.models import Brand,Category,SubCategory
from django.contrib.auth import get_user_model 
from django.core.files.uploadedfile import SimpleUploadedFile
from product.models import Product
from django.urls import reverse


class TestProductBase(APITestCase) : 
    @classmethod
    def setUpTestData(self) -> None : 
        self.image = Path(__file__).parent.parent.parent / "static/test.jpg"
        self.brand = Brand.objects.create(name="brand 1")
        self.category = Category.objects.create(name="category 1")
        self.sub_category = SubCategory.objects.create(name="sub category 1",category=self.category)
        self.staff_user = get_user_model().objects.create(email="staff@gmail.com",is_staff=True)
        self.data = {
            "name": "product test",
            "price": 10,
            "introduction": "product introduction ",
            "sub_category" : self.sub_category.id,
            "brand" : self.brand.id,
            "picture" : SimpleUploadedFile(
                name = "image1.jpg",
                content= open(self.image,"rb").read(),
                content_type="image/jpg"
            )
        }
        self.product = Product.objects.create(
            name = self.data["name"],
            price = self.data["price"],
            sub_category = self.sub_category,
            brand = self.brand
        )
        self.create_list_url = reverse("create-list-product")
        self.detail_url = reverse("detail-product",args=[self.product.id])