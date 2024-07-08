from settings.tests import BaseSettingCase
from django.urls import reverse

class PosterTest(BaseSettingCase)  : 

    @classmethod
    def setUpTestData(self) : 
        super().setUpTestData()
        self.poster_list_url = reverse("poster-list")
        self.poster_detail_url = reverse("poster-detail",args=[self.poster_1.id])
    
    def test_create(self) : 
        self.client.force_authenticate(self.staff_user)
        response = self.client.post(self.poster_list_url,self.data)
        self.assertEqual(response.status_code,201)
        self.assertEqual(self.settings.posters.count(),2)
    
    def test_get(self) : 
        response = self.client.get(self.poster_list_url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data[0]["id"],self.poster_1.id)
    
    def test_permission(self) : 
        self.client.force_authenticate(self.user)
        response = self.client.post(self.poster_list_url,data=self.data)
        self.assertEqual(response.status_code,403)