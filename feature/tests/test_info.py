from feature.tests import BaseTest

class TestFeature(BaseTest) : 

    def test_list_info(self) : 
        response = self.client.get(self.list_info_url)
        self.assertEqual(response.status_code , 200)
        self.assertEqual(response.data[0]["id"],self.info.id)
    
    def test_permission_for_create(self) : 
        self.client.force_authenticate(self.user)
        response = self.client.post(self.list_info_url)
        self.assertEqual(response.status_code,403)
    
    def test_create_info(self) : 
        self.client.force_authenticate(self.staff_user)
        response = self.client.post(self.list_info_url,{
            "product" : self.product.id ,
            "name" : "name 2",
            "value" : "value 2"
        })
        self.assertEqual(response.status_code,201)
    
    def test_get_info(self) : 
        response = self.client.get(self.info_detail_url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data["id"],self.info.id)
    
    def test_update_info(self) : 
        self.client.force_authenticate(self.staff_user)
        response = self.client.put(self.info_detail_url,{"name" : "name 1 edited"})
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data["name"],"name 1 edited")
    
    def test_delete_info(self) : 
        self.client.force_authenticate(self.staff_user)
        response = self.client.delete(self.info_detail_url)
        self.assertEqual(response.status_code,204)