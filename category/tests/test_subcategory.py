from category.tests import TestBase
from django.urls import reverse
from category.models import SubCategory,Category
from django.core.files.uploadedfile import SimpleUploadedFile
from product.models import Product


class SubCategoryTest(TestBase) : 
    @classmethod
    def setUpTestData(self) : 
        super().setUpTestData()
        self.category = Category.objects.create(name=self.data_2["name"],image=self.data_2["image"])
        self.url_list = reverse("list-sub-categories")
        self.url_detail = reverse("detail-sub-category",args=[self.category.id])
        self.data_3 = {
            "name" : "item 3",
            "image" : SimpleUploadedFile(
                name= "test3.jpg",
                content=open(self.image,"rb").read(),
                content_type="image/jpg"
                ),
            "category" : self.category.id
        }
        self.sub_category = SubCategory.objects.create(
            name = self.data.get("name"),
            image = self.data.get("image"),
            category = self.category
        )
        self.product = Product.objects.create(
            name = "product 1",
            price = 1500,
            sub_category = self.sub_category
        )
        
    ########### detail ##########
        
    def test_permission(self) : 
        response = self.client.post(self.url_list,data=self.data)
        self.assertEqual(response.status_code,401)
        
        
    def test_create(self) : 
        self.client.force_authenticate(self.staff_user)
        response = self.client.post(self.url_list,data=self.data_3)    
        self.assertEqual(response.status_code,201)
    
    def test_get_list(self) : 
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code,200)
    
    ########### detail ##########
    
    def test_put(self) : 
        self.client.force_authenticate(self.staff_user)
        response = self.client.put(self.url_detail,data={"name" : "item edited"})
        self.assertEqual(response.status_code,200)
    
    def test_delete(self) : 
        self.client.force_authenticate(self.staff_user)
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code,204) 
    
    def test_get(self) : 
        response = self.client.get(self.url_detail)
        keys = response.data.keys()
        self.assertEqual(response.status_code,200)
        self.assertIn("category",keys)
        self.assertIn("name",keys)
        self.assertIn("id",keys)
        self.assertIn("image",keys)
        self.assertIn("products",keys)