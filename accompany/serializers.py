from rest_framework import serializers
from .models import Accompany,Comment 

class AccompanySerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    created_at = serializers.CharField(read_only=True)
    updated_at = serializers.CharField(read_only=True)

    comments = serializers.SerializerMethodField(read_only=True)

    def get_comments(self, instance):
        serializer = CommentSerializer(instance.comments, many=True)
        return serializer.data

    class Meta:
        model = Accompany
        fields = '__all__'
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "comments"
        ]
class AccompanyListSerializer(serializers.ModelSerializer):
    comments_cnt = serializers.SerializerMethodField()

    def get_comments_cnt(self, instance):
        return instance.comments.count()
    
    class Meta:
        model = Accompany
        fields = [
            "id",
            "user",
            "age",
            "travel_area",
            "travel_period",
            "description",
            "comments_cnt",
            "created_at"
        ]
        read_only_fields = ["id", "created_at", "updated_at", "comments_cnt"]


class CommentSerializer(serializers.ModelSerializer):
    anonymous_name = serializers.ReadOnlyField()  # 익명 이름은 읽기 전용 필드로 설정
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['anonymous_name', 'accompany']  