from django.urls import path, include
from rest_framework import routers
from .views import AccompanyViewSet, CommentViewSet, AccompanyCommentViewSet
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="accompany"

default_router = routers.SimpleRouter(trailing_slash=False)
default_router.register("", AccompanyViewSet, basename="accompanies" )

comment_router = routers.SimpleRouter(trailing_slash=False)
comment_router.register("comments", CommentViewSet, basename="comments")

accompany_comment_router = routers.SimpleRouter(trailing_slash=False)
accompany_comment_router.register("", AccompanyCommentViewSet, basename="comments")
urlpatterns = [
    path("", include(default_router.urls)),  # 기본 accompany URL
    path("<str:trip_type>/", AccompanyViewSet.as_view({'get': 'list'}), name="accompany_by_type"),
    path("<int:accompany_id>/comments/", include(accompany_comment_router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)