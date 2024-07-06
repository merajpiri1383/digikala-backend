from django.urls import path 
from feature import views 

urlpatterns = [
    path("<id>/info/",views.ListCreateInfoAPIView.as_view(),name="info"),
    path("<id>/info/<info_id>/",views.InfoAPIView.as_view(),name="info-detail"),
]