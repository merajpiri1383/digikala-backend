from django.urls import path
from category import views

urlpatterns = [
    path("",views.CreateListBrandAPIView.as_view()),
    path("<slug:slug>/",views.CategoryAPIView.as_view()),
    path("brand/",views.CreateListBrandAPIView.as_view()),
    path("brand/<slug:slug>/",views.BrandAPIView.as_view()),
]