from feature.tests import BaseTest
from django.urls import reverse 
from feature.models import Info,SubInfo

class InfoTest(BaseTest) : 

    @classmethod 
    def setUpTestData(self) : 
        super().setUpTestData()
        self.info = Info.objects.create(name="info 1 ",product=self.product)
        self.sub_info = SubInfo.objects.create(
            info = self.info ,
            name = "sub info 1",
            value = "sub info 1"
        )
        self.list_create_info_url = reverse("info-list",args=[self.product.id])
        self.info_detail_url = reverse("info-detail",args=[self.info.id])
        self.sub_info_detail = reverse("sub-info-detail",args=[self.sub_info.id])
    
    def test_list_info(self) : 
        response = self.client.get(self.list_create_info_url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data[0]["id"] , self.info.id)
     
    def test_create_info(self) : 
        self.client.force_authenticate(self.staff_user)
        response = self.client.post(self.list_create_info_url,{"name":"info 2","value" : "value 2"})
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.data["name"],"info 2")
    

    ################### info detail 

    def test_get_info(self) : 
        response = self.client.get(self.info_detail_url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data["id"],self.info.id)
    
    def test_update_info(self) : 
        self.client.force_authenticate(self.staff_user)
        response = self.client.put(self.info_detail_url,{"name":"info 1 edted"})
        self.assertEqual(response.status_code,200)
    
    #################### sub info detail

    def test_get_sub_info(self) : 
        response = self.client.get(self.sub_info_detail)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data["id"],self.sub_info.id)