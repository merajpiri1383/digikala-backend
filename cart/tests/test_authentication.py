from cart.tests import CartBaseTest 

class TestAuthenticationCart(CartBaseTest) :
    
    def test_for_not_authenticated(self) : 
        response = self.client.post(self.cart_product_url,data={"id" : self.product.id})
        self.assertEqual(response.status_code,401)
    
    def test_for_authenticated(self) : 
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.cart_product_url,data={"id" : self.product.id})
        self.assertEqual(response.status_code,201)