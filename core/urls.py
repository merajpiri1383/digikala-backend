from django.contrib import admin
from django.urls import path,include,re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf import settings 
from django.views.static import serve

urlpatterns = [
    re_path(r"^media/(?P<path>.*)$",serve,{"document_root" : settings.MEDIA_ROOT}),
    path('admin/', admin.site.urls),
    path("account/",include('authentication.urls')),
    path("category/",include("category.urls")),
    path("product/",include("product.urls")),
    path("cart/",include("cart.urls")),
    path("user/",include("user.urls")),
    path("feature/",include("feature.urls")),
    path("settings/",include("settings.urls")),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]