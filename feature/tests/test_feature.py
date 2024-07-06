from feature.tests import BaseTest
from django.urls import reverse
from feature.models import Feature

class TestFeature(BaseTest) : 

    @classmethod
    def setUpTestData(self) : 
        super().setUpTestData()
        self.list_feature_url = reverse("feature",args=[self.product.id])
        self.feature = Feature.objects.create(
            product = self.product,
            name = "name 1", 
            value = "value 1"
        )
        self.feature_detail_url = reverse("feature-detail",args=[self.product.id,self.feature.id])

    def test_list_feature(self) : 
        response = self.client.get(self.list_feature_url)
        self.assertEqual(response.status_code , 200)
        self.assertEqual(response.data[0]["id"],self.feature.id)
    
    def test_permission_for_create(self) : 
        self.client.force_authenticate(self.user)
        response = self.client.post(self.list_feature_url)
        self.assertEqual(response.status_code,403)
    
    def test_create_feature(self) : 
        self.client.force_authenticate(self.staff_user)
        response = self.client.post(self.list_feature_url,{
            "product" : self.product.id ,
            "name" : "name 2",
            "value" : "value 2"
        })
        self.assertEqual(response.status_code,201)
     
    def test_get_feature(self) : 
        response = self.client.get(self.feature_detail_url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data["id"],self.feature.id)
    
    def test_update_feature(self) : 
        self.client.force_authenticate(self.staff_user)
        response = self.client.put(self.feature_detail_url,{"name" : "name 1 edited"})
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data["name"],"name 1 edited")
    
    def test_delete_feature(self) : 
        self.client.force_authenticate(self.staff_user)
        response = self.client.delete(self.feature_detail_url)
        self.assertEqual(response.status_code,204)