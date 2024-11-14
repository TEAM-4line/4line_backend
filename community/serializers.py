from rest_framework import serializers
from .models import *
class CommunitySerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(read_only=True)  # source 제거
    scrap_count = serializers.IntegerField(read_only=True)  # source 제거

    class Meta:
        model = Community
        fields = ['id', 'title', 'trip_time', 'cost', 'region', 'rating', 'content', 'photo', 'like_count', 'scrap_count', 'created_at']
