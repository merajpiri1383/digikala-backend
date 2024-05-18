from django.test import TestCase
from category.models import Brand,Category
from django.utils.text import slugify
from rest_framework.test import APIClient,APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class BrandTest(APITestCase) :
    
    def setUp(self) :
        self.brand = Brand.objects.create(name="brand 1")
        self.user = get_user_model().objects.create(email="test@gmail.com")
        self.staff_user = get_user_model().objects.create(email="staff@gmail.com",is_staff=True)
        self.list_url = reverse("create-list-category")
        
    def tearDown(self) -> None : 
        self.brand.delete()
    
    def test_slug_of_brand(self) :
        self.assertEqual(self.brand.slug,slugify(self.brand.name,allow_unicode=True))

    def test_permission_for_staff_user(self):
        self.client.force_authenticate(user=self.staff_user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code,200)

    def test_permission_for_normal_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code,403)


class CategoryTest(APITestCase) :
    
    def setUp(self) : 
        self.category = Category.objects.create(name="category 1")
        self.user = get_user_model().objects.create(email="test@gmail.com")
        self.staff_user = get_user_model().objects.create(email="staff@gmail.com", is_staff=True)
        self.list_url = reverse("create-list-category")
    
    def tearDown(self) -> None : 
        self.category.delete()
    
    def test_slug_of_category(self) : 
        self.assertEqual(self.category.slug,slugify(self.category.name,allow_unicode=True))

    def test_permission_for_staff_user(self):
        self.client.force_authenticate(user=self.staff_user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code,200)

    def test_permission_for_normal_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code,403)