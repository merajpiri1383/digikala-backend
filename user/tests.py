from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from user.serializers import UserSerializer

class TestUser(APITestCase) : 
    @classmethod
    def setUpTestData(self) : 
        self.user = get_user_model().objects.create(email="test@gmail.com")
        self.user_url = reverse("user")
    
    
    def test_not_authenticate_user(self) : 
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code,401)
    
    def test_get_data(self) :
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data,UserSerializer(self.user).data)