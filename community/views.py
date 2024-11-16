from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Community
from .serializers import CommunitySerializer
from rest_framework.permissions import IsAuthenticated

class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [IsAuthenticated]

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