from rest_framework import serializers
from .models import *
class CommunitySerializer(serializers.ModelSerializer):

    like_count = serializers.IntegerField(read_only=True)
    scrap_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Community
        fields = '__all__'

    name = serializers.SerializerMethodField()
    def get_name(self, obj):
        # writer 필드에서 사용자 이름을 가져옴
        return obj.writer.name if obj.writer.name else obj.writer.email

    def create(self, validated_data):
        # `likes`와 `scraps` 필드를 제거하고 나머지 데이터로 인스턴스 생성
        likes_data = validated_data.pop('likes', None)
        scraps_data = validated_data.pop('scraps', None)
        community = Community.objects.create(**validated_data)
        
        # `ManyToMany` 필드는 객체를 생성한 후 `.set()`으로 설정
        if likes_data:
            community.likes.set(likes_data)
        if scraps_data:
            community.scraps.set(scraps_data)
        
        return community