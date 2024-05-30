from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse 

class TestBase(APITestCase) : 
    @classmethod
    def setUpTestData(self) -> None : 
        self.user = get_user_model().objects.create(email="test@gmail.com")
        self.auth_url = reverse("auth")
        self.activate_url = reverse("activate")
        self.login_url = reverse("login")
        self.send_otp_url = reverse("send-otp")
        self.password = "Password@123"
        self.update_password_url = reverse("password-update")
        self.user.set_password(self.password)
        self.user.save()