from django.urls import path, include
from rest_framework import routers
from .views import AccompanyViewSet, CommentViewSet, AccompanyCommentViewSet
from django.conf import settings
from django.conf.urls.static import static

app_name = "accompany"

# Main router for AccompanyViewSet
default_router = routers.SimpleRouter(trailing_slash=False)
default_router.register("", AccompanyViewSet, basename="accompanies")

# Comment-specific router
comment_router = routers.SimpleRouter(trailing_slash=False)
comment_router.register("", AccompanyCommentViewSet, basename="comments")

urlpatterns = [
    # Base AccompanyViewSet URLs
    path("", include(default_router.urls)),

    # Accompany filtering by trip_type
    path("<str:trip_type>/", AccompanyViewSet.as_view({'get': 'list'}), name="accompany_by_type"),

    # Nested comments for a specific Accompany
    path("<int:accompany_id>/comments/", include(comment_router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
