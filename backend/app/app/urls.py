from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from users.views import ActivateUserEmail

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/v1/api-auth/", include("rest_framework.urls", namespace="rest_framework")
    ),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path('activate/<str:uid>/<str:token>/', ActivateUserEmail.as_view(), name='activate email'),
    # path("", include("dialogs.urls")),
    # path("api/v1/", include("users.urls")),
]
