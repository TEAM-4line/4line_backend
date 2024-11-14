from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import *

app_name = "community"

default_router = routers.SimpleRouter(trailing_slash=False)
default_router.register("post", CommunityViewSet, basename="test")

urlpatterns = [
    path("", include(default_router.urls)),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)