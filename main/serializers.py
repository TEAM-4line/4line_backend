# serializers.py
from rest_framework import serializers
from users.models import User
from community.models import Community  # Community 모델 임포트

class MainUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['name', 'trip_type']
    
    def get_name(self, obj):
        return obj.name if obj.name else obj.email

class PopularCommunitySerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(read_only=True)  # source 제거
    scrap_count = serializers.IntegerField(read_only=True)  # source 제거

    class Meta:
        model = Community
        fields = ['id', 'region', 'title','like_count','scrap_count','photo']