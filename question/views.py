from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Test  # Test 모델 import
from users.models import User  # User 모델 import
from .serializers import TestListSerializer, TestSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'list':
            return TestListSerializer
        elif self.action == 'retrieve':
            return TestSerializer
        return TestListSerializer

    def create(self, request, *args, **kwargs):
        user_id = request.data[0].get("id")  # 요청에서 사용자 ID 가져오기
        user = get_object_or_404(User, id=user_id)  # 사용자 객체 조회

        # 요청 데이터로 Test 객체 생성
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        instances = serializer.save(name=user)  # Test 객체 생성

        # 마지막 Test 객체의 trip_type을 계산하여 User 모델에 저장
        if instances:
            last_instance = instances[-1]  # 마지막 생성된 Test 객체
            user.trip_type = last_instance.trip_type
            user.save()  # User 모델 업데이트

        return Response(serializer.data, status=status.HTTP_201_CREATED)
