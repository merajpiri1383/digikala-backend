from rest_framework.test import APITestCase
from product.models import Color
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
        self.list_create_url = reverse('list-create-color')
        self.detail_url = reverse('detail-color',args=[1])
        self.staff_user = get_user_model().objects.create(email="staff@gmail.com",is_staff=True)
        self.color = Color.objects.create(name="test-color",hex="#4ewe551")


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
    
    def test_update_color(self) : 
        self.client.force_authenticate(user=self.staff_user)
        response = self.client.put(self.detail_url,data=self.data)
        self.assertEqual(response.status_code , 200)
    
    def test_get_color(self) : 
        self.client.force_authenticate(user=self.staff_user) 
        response = self.client.get(self.detail_url)
        serializer_data = ColorSerializer(self.color).data
        self.assertEqual(response.data,serializer_data)
    
    def test_delete_color(self) : 
        self.client.force_authenticate(user=self.staff_user) 
        response = self.client.delete(self.detail_url) 
        self.assertEqual(response.status_code,204)