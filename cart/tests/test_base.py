from rest_framework.test import APITestCase
from cart.models import Cart,CartProduct
from product.models import Product,Brand,Category
from django.contrib.auth import get_user_model 
from django.urls import reverse

class CartBaseTest(APITestCase) : 
    @classmethod
    def setUpTestData(self) : 
        self.user = get_user_model().objects.create(email="test@gmail.com")
        self.brand = Brand.objects.create(name="brand 1")
        self.category = Category.objects.create(name="category 1")
        self.product = Product.objects.create(
            name="product 1",
            price=15,
            brand = self.brand,
            category = self.category
        )
        self.product_2 = Product.objects.create(
            name = "product 2",
            price = 20,
            brand = self.brand,
            category = self.category
        )
        self.cart = Cart.objects.create(user=self.user)
        self.cart_product = CartProduct.objects.create(
            product = self.product,
            cart = self.cart,
            count = 3
        )
        self.cart_product_one_item = CartProduct.objects.create(
            product = self.product_2,
            cart = self.cart,
            count = 1
        )
        self.cart_product_url = reverse("cart-product-edit")