from django.shortcuts import render
from .models import Accompany, Comment
from .permissions import IsOwnerOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import AccompanySerializer, CommentSerializer, AccompanyListSerializer
# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Accompany
from .serializers import AccompanySerializer

from django.shortcuts import get_object_or_404

class AccompanyViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        trip_type = self.kwargs.get("trip_type")
        if trip_type:
            return Accompany.objects.filter(trip_type=trip_type)
        return Accompany.objects.all()
    
    def get_serializer_class(self):
        if self.action == "list":
            return AccompanyListSerializer
        return AccompanySerializer
    
    def get_permissions(self):
        if self.action in ["update", "destroy", "partial_update"]:
            return [IsAdminUser()]
        return []

    def create(self, request):
    # 현재 로그인한 유저 정보에서 trip_type 가져오기
        user = request.user
        trip_type = user.trip_type  # 유저의 trip_type 가져오기

    # 요청 데이터를 복사하여 trip_type 추가
        data = request.data.copy()
        data['trip_type'] = trip_type

    # Serializer에 수정된 데이터를 전달
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        accompany = serializer.instance  # 생성된 Accompany 인스턴스
        return Response(serializer.data)
    
    def perform_update(self, serializer):
            accompany=serializer.save()
        

        
class CommentViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ["update", "destroy", "partial_update"]:
            return [IsOwnerOrReadOnly()]
        return []

class AccompanyCommentViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    # queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        accompany = self.kwargs.get("accompany_id")
        queryset = Comment.objects.filter(accompany_id=accompany)
        return queryset

    # def list(self, request, accompany_id=None):
    #     accompany = get_object_or_404(Accompany, id = accompany_id)
    #     queryset = self.filter_queryset(self.get_queryset().filter(accompany=accompany))
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)
    
    def create(self, request, accompany_id=None):
        accompany= get_object_or_404(Accompany, id=accompany_id)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(accompany=accompany)
        return Response(serializer.data)
    

