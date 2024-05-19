from rest_framework.test import APITestCase
from product.models import Product
from product.serializers import ProductSerializer 
from category.models import Brand,Category
from django.contrib.auth import get_user_model
from django.urls import reverse
from pathlib import Path



class TestProductBase(APITestCase) : 
    image = Path(__file__).parent.parent.parent / "static/test.jpg"
    data = {
        "name": "product test",
        "price": 10,
        "introduction": "product introduction ",
        "category" : 1,
        "brand" : 1,
    }
    
    def setUp(self) -> None : 
        self.create_list_url = reverse("create-list-product")
        self.detail_url = reverse("detail-product",args=[1])
        self.brand = Brand.objects.create(name="brand 1")
        self.category = Category.objects.create(name="category 1")
        self.staff_user = get_user_model().objects.create(email="staff@gmail.com",is_staff=True)
        self.product = Product.objects.create(
            name = self.data["name"],
            price = self.data["price"],
            category = self.category,
            brand = self.brand
        )
    
    def tearDown(self) -> None : 
        self.brand.delete()
        self.category.delete()
        self.staff_user.delete()

class TestProductPermissions(TestProductBase) : 
    def setUp(self) : 
        self.user = get_user_model().objects.create(email="test@gmail.com")
        super().setUp()
    
    def tearDown(self) -> None : 
        self.user.delete()
        super().tearDown()
        
    def test_permissions_for_normal_user(self) : 
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.create_list_url)
        self.assertEqual(response.status_code,403)
        
        
    def test_permissions_for_staff_user(self) : 
        self.client.force_authenticate(user=self.staff_user) 
    
    def test_permission_for_normal_user_in_get_method(self) : 
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.create_list_url)
        self.assertEqual(response.status_code,200)
    
    def test_permission_for_not_authenticate_user(self) : 
        response = self.client.get(self.create_list_url)
        self.assertEqual(response.status_code,200)

class TestProductListCreate(TestProductBase) : 
    
    def test_create_product(self) : 
        self.client.force_authenticate(user=self.staff_user)
        with open(self.image,"rb") as image : 
            self.data["picture"] = image
            response = self.client.post(self.create_list_url,data=self.data)
            self.assertEqual(response.status_code,201)
    
    def test_list_product(self) : 
        response = self.client.get(self.create_list_url)
        serializer_data = ProductSerializer([self.product],many=True).data 
        self.assertEqual(response.data,serializer_data)
        self.assertEqual(response.status_code,200)


class TestProductDetail(TestProductBase) : 
    
    def test_get_product(self) : 
        response = self.client.get(self.detail_url)
        serializer_data = ProductSerializer(Product.objects.get(name=self.data["name"])).data 
        self.assertEqual(serializer_data,response.data)
        self.assertEqual(response.status_code,200)
    
    def test_delete_product(self) : 
        self.client.force_authenticate(user=self.staff_user) 
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code,204)
    
    def test_put_product(self) : 
        self.client.force_authenticate(user=self.staff_user)
        with open(self.image,"rb") as image : 
            self.data["picture"] = image
            response = self.client.put(self.detail_url,data=self.data)
            self.assertEqual(response.status_code,200)