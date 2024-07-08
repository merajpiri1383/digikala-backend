from django.urls import path
from settings import views

urlpatterns = [
    path("poster/",views.PosterListCreateAPIView.as_view(),name="poster-list"),
    path("poster/<int:id>/",views.PosterDestroyAPIView.as_view(),name="poster-detail"),
]