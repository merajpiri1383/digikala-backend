from cart.tests import CartBaseTest
from cart.serializers import CartProductSerializer,CartSerializer

class TestCartView(CartBaseTest) : 
    
    def test_add_product_to_cart(self) : 
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.cart_product_url,data={"id":self.product.id})
        self.assertEqual(response.status_code,201)
    
    def test_delete_product_from_cart_one_item(self) : 
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.cart_product_url,data={"id":self.product_2.id})
        self.assertNotIn(CartProductSerializer(self.cart_product_one_item).data , response.data["cart_products"])
        self.assertEqual(response.status_code,200)
    
    def test_delete_product_from_cart_many_item(self) : 
        self.client.force_authenticate(user=self.user) 
        self.cart_product.count -= 1 
        self.cart_product.save()
        response = self.client.delete(self.cart_product_url,data={"id":self.product.id})
        self.assertEqual(response.data["cart_products"], CartSerializer(self.cart).data["cart_products"])
        self.assertEqual(response.status_code,200)