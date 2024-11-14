from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializers import *
'''
class TestViewSet(viewsets.ModelViewSet):
    queryset = Totaltest.objects.all()
    serializer_class = TestSerializer # 인증된 사용자만 접근 가능하도록 설정

    def perform_create(self, serializer):
        # 요청한 사용자를 writer로 설정하고 인스턴스 생성
        serializer.save(writer=self.request.user)
'''
class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':  # 상세 조회 시
            return TestSerializer
        return TestListSerializer

