from django.test import TestCase
from category.models import Brand,Category
from django.utils.text import slugify
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model 
from rest_framework_simplejwt.tokens import RefreshToken

class BrandTest(TestCase) : 
    
    def setUp(self) : 
        self.client = APIClient()
        self.brand = Brand.objects.create(name="brand 1")
        self.user = get_user_model().objects.create(email="test@gmail.com",is_staff=True)
        self.token = RefreshToken.for_user(self.user)
        self.client.defaults.setdefault("Authorization",f"Bearer {self.token.access_token}")
        # self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token.access_token}")
        
    def tearDown(self) -> None : 
        self.brand.delete()
    
    def test_slug_of_brand(self) :        
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token.access_token}")
        self.client.login(credentials={})
        self.assertEqual(self.brand.slug,slugify(self.brand.name,allow_unicode=True))
    

class CategoryTest(TestCase) : 
    
    def setUp(self) : 
        self.category = Category.objects.create(name="category 1")
    
    def tearDown(self) -> None : 
        self.category.delete()
    
    def test_slug_of_category(self) : 
        self.assertEqual(self.category.slug,slugify(self.category.name,allow_unicode=True))
    