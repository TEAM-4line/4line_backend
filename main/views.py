# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from community.models import Community
from .serializers import MainUserSerializer, PopularCommunitySerializer
from django.db.models import Count
from rest_framework.permissions import IsAuthenticated

class MainPageView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # 1. 사용자 정보 가져오기
        user = request.user
        user_serializer = MainUserSerializer(user)

        # 2. 좋아요가 많은 상위 2개의 커뮤니티 게시물 가져오기
        popular_communities = Community.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:2]
        community_serializer = PopularCommunitySerializer(popular_communities, many=True)

        # 3. 데이터를 통합하여 응답 생성
        response_data = {
            'user_info': user_serializer.data,
            'popular_communities': community_serializer.data
        }

        return Response(response_data)
