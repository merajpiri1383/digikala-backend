from django.urls import path
from category import views

urlpatterns = [
    path("",views.CreateListCategoryAPIView.as_view(),name="create-list-category"),
    path("<slug:slug>/",views.CategoryAPIView.as_view(),name="category-detail"),
    path("brand/",views.CreateListBrandAPIView.as_view(),name="create-list-brand"),
    path("brand/<slug:slug>/",views.BrandAPIView.as_view(),name="brand-detail"),
]