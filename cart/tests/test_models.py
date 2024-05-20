
from cart.tests import CartBaseTest

class CartModelTest(CartBaseTest) : 
    
    def test_total_price_in_cart(self) : 
        t = self.cart_product.count * self.product.price+self.cart_product_one_item.count * self.product_2.price
        self.assertEqual(self.cart.total,t)