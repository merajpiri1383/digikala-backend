from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product 

class Cart(models.Model) : 
    user = models.ForeignKey(get_user_model(),related_name="carts",on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    
    @property 
    def total(self) : 
        t = 0 
        for cart_product in self.cart_products.all() : 
            t += cart_product.total_price 
        return t

class CartProduct(models.Model) : 
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="cart_products")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    
    @property 
    def total_price(self) : 
        return self.product.price * self.count 