
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("cart/", include("cart.urls")),
    path("orders/", include("orders.urls")),
    path("shop/", include("shop.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("admin/", admin.site.urls),
    path("", include("homepage.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
