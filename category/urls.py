from django.urls import path
from category import views

urlpatterns = [
    path("sub-category/<pk>/",views.SubCategoryAPIView.as_view(),name="detail-sub-category"),
    path("brand/",views.CreateListBrandAPIView.as_view(),name="create-list-brand"),
    path("brand/<pk>/",views.BrandAPIView.as_view(),name="brand-detail"),
    path("sub-category/",views.ListCreateSubCategoryAPIView.as_view(),name="list-sub-categories"),
    path("",views.CreateListCategoryAPIView.as_view(),name="create-list-category"),
    path("<pk>/",views.CategoryAPIView.as_view(),name="category-detail"),
    path("<id>/poster/",views.PosterCategoryCreateListAPIView.as_view(),name="poster-category-list"),
    path("poster/<pk>/",views.PosterCategoryDetailAPIView.as_view(),name="poster-category-detail"),
] 