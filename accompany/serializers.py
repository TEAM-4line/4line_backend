from rest_framework import serializers
from .models import Accompany,Comment 

class AccompanySerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    user_name = serializers.CharField(source='user.name', read_only=True)
    profile_image = serializers.CharField(source='user.profile_image', read_only=True)  # profile_image 추가
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)  # 포맷팅 추가
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)  # 포맷팅 추가
    comments = serializers.SerializerMethodField(read_only=True)

    def get_comments(self, instance):
        serializer = CommentSerializer(instance.comments, many=True)
        return serializer.data

    class Meta:
        model = Accompany
        fields = fields = [
            "id",
            "user_name",
            "profile_image",
            "created_at",
            'updated_at',
            "comments",
            "trip_type",
            "age",
            "travel_area",
            "travel_period",
            "description",
            "user"
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "comments"
            "trip_type"
        ]
class AccompanyListSerializer(serializers.ModelSerializer):
    comments_cnt = serializers.SerializerMethodField()
    user_name = serializers.CharField(source='user.name', read_only=True) 
    profile_image = serializers.CharField(source='user.profile_image', read_only=True)  # profile_image 추가
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)  # 포맷팅 추가

    def get_comments_cnt(self, instance):
        return instance.comments.count()
    
    class Meta:
        model = Accompany
        fields = [
            "id",
            "user",
            "user_name",
            "profile_image",
            "age",
            "travel_area",
            "travel_period",
            "description",
            "comments_cnt",
            "created_at",
            "trip_type"
        ]
        read_only_fields = ["trip_type", "id", "created_at", "updated_at", "comments_cnt"]


class CommentSerializer(serializers.ModelSerializer):
    anonymous_name = serializers.ReadOnlyField()  # 익명 이름은 읽기 전용 필드로 설정
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)  # 포맷팅 추가
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['anonymous_name', 'accompany']  