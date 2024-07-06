from feature.tests import BaseTest
from django.urls import reverse 
from feature.models import Info,SubInfo

class InfoTest(BaseTest) : 

    @classmethod 
    def setUpTestData(self) : 
        super().setUpTestData()
        self.info = Info.objects.create(name="info 1 ",product=self.product)
        self.list_create_info_url = reverse("info",args=[self.product.id])
    
    def test_list_info(self) : 
        response = self.client.get(self.list_create_info_url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data[0]["id"] , self.info.id)
    
    def test_create_info(self) : 
        self.client.force_authenticate(self.staff_user)
        response = self.client.post(self.list_create_info_url,{"name":"info 2","value" : "value 2"})
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.data["name"],"info 2")