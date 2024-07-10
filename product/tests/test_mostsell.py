from product.tests import TestProductBase
from django.urls import reverse

class MostSellProductTest(TestProductBase) : 
    
    @classmethod
    def setUpTestData(self) : 
        super().setUpTestData()
        self.most_sell_url = reverse("most-sell")
        self.most_sell_category_url = reverse("most-sell-category",args=[self.category.id])
    

    def test_get_most_sell(self) : 
        response = self.client.get(self.most_sell_url)
        self.assertEqual(response.status_code,200)
    
    def test_get_most_sell_for_category(self) :
        response = self.client.get(self.most_sell_category_url)
        self.assertEqual(response.status_code,200)