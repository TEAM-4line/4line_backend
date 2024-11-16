from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status, filters
from .models import Community
from .serializers import CommunitySerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter, NumberFilter

# 여행 기간 필터 정의
class CommunityFilter(FilterSet):
    #trip_time = CharFilter(method='filter_trip_time', label='Trip Time')
    trip_time = NumberFilter(field_name='trip_time', lookup_expr='exact', label='Trip Time')
    trip_timeUnit = CharFilter(field_name='trip_timeUnit', lookup_expr='exact', label='Trip Time Unit')

    class Meta:
        model = Community
        fields = ['trip_time', 'trip_timeUnit']

    # 여행 기간을 '일', '주', '개월'로 필터링
    def filter_trip_time(self, queryset, name, value):
        if value.endswith("일"):
            return queryset.filter(trip_time__contains="일")
        elif value.endswith("주"):
            return queryset.filter(trip_time__contains="주")
        elif value.endswith("개월"):
            return queryset.filter(trip_time__contains="개월")
        return queryset.none()
    
class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = CommunityFilter
    ordering_fields = ['created_at', 'updated_at']


    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)
        

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        community = self.get_object()
        user = request.user

        if user in community.likes.all():
            community.likes.remove(user)
            return Response({'status': 'like removed'}, status=status.HTTP_200_OK)
        else:
            community.likes.add(user)
            return Response({'status': 'like added'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def scrap(self, request, pk=None):
        community = self.get_object()
        user = request.user

        if user in community.scraps.all():
            community.scraps.remove(user)
            return Response({'status': 'scrap removed'}, status=status.HTTP_200_OK)
        else:
            community.scraps.add(user)
            return Response({'status': 'scrap added'}, status=status.HTTP_200_OK)