from django.urls import path, include
from rest_framework import routers
from .views import *

app_name = "question"

default_router = routers.SimpleRouter(trailing_slash=False)
default_router.register("test", TestViewSet, basename="test")
# URL 패턴
urlpatterns = [
    path("", include(default_router.urls)),  # 등록된 모든 ViewSet의 URL 포함
]
