from django.urls import path, include
from rest_framework import routers
from .views import AccompanyViewSet, AccompanyCommentViewSet, CommentViewSet, AccompanyByTypeView
from django.conf import settings
from django.conf.urls.static import static

app_name = "accompany"

# Main router for AccompanyViewSet
default_router = routers.SimpleRouter(trailing_slash=True)
default_router.register("", AccompanyViewSet, basename="accompanies")

urlpatterns = [
    # 여행 타입별 게시물 조회
    #path("<str:trip_type>/", AccompanyViewSet.as_view({'get': 'list'}), name="accompany_by_type"),
    path("<str:trip_type>/", AccompanyByTypeView.as_view(), name="accompany_by_type"),

    # Base AccompanyViewSet URLs
    path("", include(default_router.urls)),

   #댓글 관련
    path("<int:accompany_id>/comments/", AccompanyCommentViewSet.as_view({'get': 'list', 'post': 'create'}), name="accompany_comments"),
    path( "<int:accompany_id>/comments/<int:pk>/", CommentViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name="delete_comment")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)