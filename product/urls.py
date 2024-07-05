from django.urls import path
from product import views

urlpatterns = [
    ######################### color ##############################
    path("color/",views.CreateColorAPIView.as_view(),name="list-create-color"),
    path("color/<int:pk>/",views.ColorAPIView.as_view(),name="detail-color"),
    ######################### product ############################
    path("",views.CreateListProductAPIView.as_view(),name="create-list-product"),
    path("<pk>/",views.ProductAPIView.as_view(),name="detail-product"),
    path("<pk>/image/<image_id>/",views.ImageProductAPIView.as_view(),name="product-image-delete"),
    path("<pk>/image/",views.ImageProductAPIView.as_view(),name="product-image"),
]