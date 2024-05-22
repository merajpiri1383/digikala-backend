from django.urls import path
from authentication import views 
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("activate/",views.ActivateEmailAPIView.as_view(),name="activate"),
    path("auth/",views.AuthAPIView.as_view(),name="auth"),
    path("token/refresh/",TokenRefreshView.as_view()),
    path("login/",views.LoginAPIView.as_view(),name="login"),
    path("password/update/",views.ChangePasswordAPIView.as_view(),name="password-update")
]