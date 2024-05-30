from category.tests import TestBase
from category.models import Brand
from django.urls import reverse



class BrandTest(TestBase) :
    @classmethod
    def setUpTestData(self) :
        super().setUpTestData()
        self.brand = Brand.objects.create(name="brand 1")
        self.list_url = reverse("create-list-category")

    def test_permission_for_staff_user_post_method(self):
        self.client.force_authenticate(user=self.staff_user) 
        with open(self.image , "rb") as Image : 
            response = self.client.post(self.list_url,data={'name':self.data.get("name"),'image':Image})
        self.assertEqual(response.status_code,201)

    def test_permission_for_normal_user_post_method(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.list_url)
        self.assertEqual(response.status_code,403)
    
    def test_permission_for_not_authenticated_user_get_method(self) : 
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code,200)
    