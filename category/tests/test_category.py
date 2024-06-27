from category.tests import TestBase
from django.urls import reverse
from category.models import Category,SubCategory

class CategoryTest(TestBase) :
    
    
    @classmethod
    def setUpTestData(self) : 
        super().setUpTestData()
        self.category = Category.objects.create(name=self.data_2["name"],image=self.data_2["image"])
        self.list_url = reverse("create-list-category")
        self.get_category_url = reverse("category-detail",args=[self.category.id])
    

    def test_permission_for_staff_user(self):
        self.client.force_authenticate(user=self.staff_user)
        response = self.client.post(self.list_url,data=self.data)
        self.assertEqual(response.status_code,201)

    def test_permission_for_normal_user(self) -> None:
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.list_url)
        self.assertEqual(response.status_code,403)
    
    def test_serializer_data(self) -> None :
        response = self.client.get(self.get_category_url).data
        keys = self.client.get(self.get_category_url).data.keys()
        self.assertIn("name",keys)
        self.assertIn("id",keys)
        self.assertIn("image",keys)
        self.assertIn("sub_categories",keys)
    
    def test_put(self) -> None : 
        self.client.force_authenticate(self.staff_user)
        response = self.client.put(self.get_category_url,data={})
        self.assertEqual(response.status_code,200)