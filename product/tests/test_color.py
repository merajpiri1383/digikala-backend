from rest_framework.test import APITestCase
from product.tests import TestProductBase
from product.models import Color,Product
from django.urls import reverse
from django.contrib.auth import get_user_model
# serializers 
from product.serializers import ColorSerializer


class BaseColorTest(APITestCase) :
    
    data = {
        "name" : "color 1",
        "hex" : "ffffff"
    }
    @classmethod
    def setUpTestData(self):
        self.color = Color.objects.create(name="test-color",hex="#4ewe551")
        self.list_create_url = reverse('list-create-color')
        self.detail_url = reverse('detail-color',args=[1])
        self.staff_user = get_user_model().objects.create(email="staff@gmail.com",is_staff=True)


class ColorTestPermissions(BaseColorTest) :
    
    @classmethod
    def setUpTestData(self):
        super().setUpTestData()
        self.user = get_user_model().objects.create(email="test@gmail.com")


    def test_permission_for_staff_user(self):
        self.client.force_authenticate(user=self.staff_user)
        response = self.client.post(self.list_create_url,data=self.data)
        self.assertEqual(response.status_code,201)

    def test_permission_for_normal_user(self) -> None :
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.list_create_url)
        self.assertEqual(response.status_code,403)


class ColorTestListCreate(BaseColorTest) :
    def test_create_new_color(self) -> None:
        self.client.force_authenticate(user=self.staff_user)
        data = {
            "name": "color 1",
            "hex": "fffff"
        }
        response = self.client.post(self.list_create_url, data=data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_list_color(self) -> None:
        self.client.force_authenticate(user=self.staff_user)
        response = self.client.get(self.list_create_url)
        serializer_data = ColorSerializer([self.color],many=True).data 
        self.assertEqual(serializer_data,response.data)
    

class ColorTestDetail(BaseColorTest) : 
    
    def test_delete_color(self) : 
        self.client.force_authenticate(user=self.staff_user) 
        response = self.client.delete(self.detail_url) 
        self.assertEqual(response.status_code,204)
    

class TestColorProduct(TestProductBase) : 
    
    @classmethod 
    def setUpTestData(self) : 
        super().setUpTestData()
        self.color = Color.objects.create(name="color 1",hex="hsd5dsf")
        self.color_2 = Color.objects.create(name="colro_2",hex="sd5s7ds")
        self.product.colors.add(self.color_2)
        self.color_product_url = reverse("product-color",args=[self.product.id,self.color.id])

    def test_add_color_to_product(self) :
        self.client.force_authenticate(self.staff_user)
        response = self.client.post(self.color_product_url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(self.product.colors.count(),2)
    
    def test_remove_color_to_product(self) : 
        self.client.force_authenticate(self.staff_user)
        response = self.client.delete(self.color_product_url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(self.product.colors.count(),1)