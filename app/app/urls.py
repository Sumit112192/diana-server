from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


urlpatterns = [
    # Admin App
    path("admin/", admin.site.urls),
    # Core app
    path("", include("core.urls")),
    # Accounts app
    path("accounts/", include("accounts.urls")),
    # API Docs
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "dev/api/schema/swagger-ui",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "dev/api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
