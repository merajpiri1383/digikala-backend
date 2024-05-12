from django.urls import path
from authentication import views 

urlpatterns = [
    path("register/",views.RegisterAPIView.as_view()),
]