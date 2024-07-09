from category.tests import TestBase
from category.models import Category,PosterCategory
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

class PosterCategoryTest(TestBase) : 

    @classmethod
    def setUpTestData(self) : 
        super().setUpTestData()
        self.category = Category.objects.create(
            name = self.data["name"],
            image = self.data["image"]
        )
        self.poster_category = PosterCategory.objects.create(
            category = self.category,
            image = self.data_2["image"]
        )
        self.list_create_url = reverse("poster-category-list",args=[self.category.id])
        self.detail_url = reverse("poster-category-detail",args=[self.poster_category.id])
        self.data_3 = {
            "category" : self.category.id,
            "image" : SimpleUploadedFile(
                name="image_3.jpg",
                content= open(self.image,"rb").read(),
                content_type="image/jpg"
            )
        }


    
    def test_get_posters(self) : 
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data[0]["id"],self.poster_category.id)
    
    def test_post_poster(self) : 
        self.client.force_authenticate(self.staff_user)
        response = self.client.post(self.list_create_url,data=self.data_3)
        self.assertEqual(response.status_code,201)
        self.assertEqual(self.category.posters.count(),2)
    
    def test_delete_poster(self) : 
        self.client.force_authenticate(self.staff_user)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code,204)