from django.urls import path 
from feature import views 

urlpatterns = [
    ###### feature
    path("<int:id>/",views.ListCreateFeatureAPIView.as_view(),name="feature"),
    path("<int:id>/<int:feature_id>/",views.FeatureAPIView.as_view(),name="feature-detail"),
    ###### info
    path("<int:id>/info/",views.ListCreateInfoAPIView.as_view(),name="info"),
] 