from rest_framework.test import APITestCase
from product.models import Product
from feature.models import Feature
from category.models import SubCategory,Category
from django.contrib.auth import get_user_model
from django.urls import reverse

class BaseTest(APITestCase) : 

    @classmethod
    def setUpTestData(self) -> None:
        self.category = Category.objects.create(name="category 1")
        self.sub_category = SubCategory.objects.create(category=self.category,name="sub category 1")
        self.product = Product.objects.create(
            name = "product 1",
            price = 150,
            sub_category=self.sub_category
        )
        self.staff_user = get_user_model().objects.create(email="test_staff@gmail.com",is_staff=True)
        self.user = get_user_model().objects.create(email="test@gmail.com")