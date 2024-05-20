from django.urls import path 
from cart import views 

urlpatterns = [
    path("",views.CartProductAPIView.as_view(),name="cart-product-edit")
] 