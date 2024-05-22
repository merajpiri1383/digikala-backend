from django.urls import path
from authentication import views 
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("activate/",views.ActivateEmailAPIView.as_view()),
    path("login/",views.LoginAPIView.as_view()),
    path("token/refresh/",TokenRefreshView.as_view()),
]