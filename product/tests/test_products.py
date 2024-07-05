from rest_framework.test import APITestCase
from product.models import Product,Image
from product.serializers import ProductSerializer 
from category.models import Brand,Category,SubCategory
from django.contrib.auth import get_user_model
from django.urls import reverse
from pathlib import Path
from django.core.files.uploadedfile import SimpleUploadedFile



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

class TestProductPermissions(TestProductBase) : 
    @classmethod
    def setUpTestData(self) : 
        super().setUpTestData()
        self.user = get_user_model().objects.create(email="test@gmail.com")
        
    def test_permissions_for_normal_user(self) :
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.create_list_url,self.data)
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
        response = self.client.put(self.detail_url,data=self.data)
        self.assertEqual(response.status_code,200)

class ImageProductTest(TestProductBase) :

    @classmethod
    def setUpTestData(self) : 
        super().setUpTestData()
        self.image_product = Image.objects.create(
            product = self.product,
            picture = self.data.get("picture")
        )
        self.delete_image_url = reverse("product-image-delete",args=[self.product.id,self.image_product.id])
        self.image_url = reverse("product-image",args=[self.product.id])

    def test_add_image(self) : 
        self.client.force_authenticate(self.staff_user)
        self.client.post(self.image_url,data={"picture" : self.data.get("picture")})
        self.assertEqual(self.product.images.count() , 1)
    
    def test_delete_image(self) : 
        self.client.force_authenticate(self.staff_user)
        self.client.delete(self.delete_image_url)
        self.assertEqual(self.product.images.count(),0)