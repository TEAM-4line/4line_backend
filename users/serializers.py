from rest_framework.serializers import ModelSerializer
from .models import User, Bookmarked, PreviousTrips
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.conf import settings

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        trip_type = self.user.trip_type if self.user.trip_type else "default_trip_type"

        # 사용자 정보 추가하여 응답 확장
        data.update({
            'id': self.user.id,
            'name': self.user.name,
            'trip_type': trip_type
        })

        return data

class UserSerializer(ModelSerializer):
    trip_type = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'name', 'birth', 'email', 'password', 'intro', 'trip_type', 'profile_image']  # 필드 명 수정 및 추가
        extra_kwargs = {'password': {'write_only': True}}  # 비밀번호는 쓰기 전용으로 설정

    # 회원가입
    def create(self, validated_data):
        user = super().create(validated_data)
        password = validated_data.get('password')
        user.set_password(password)
        user.save()
        return user

    # 로그인 시 비밀번호 갱신 (만약 업데이트가 필요한 경우)
    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        password = validated_data.get('password')
        if password:
            user.set_password(password)
            user.save()
        return user
    
class BookmarkedSerializer(ModelSerializer):
    class Meta:
        model = Bookmarked
        fields = ['content']

class PreviousTripsSerializer(ModelSerializer):
    class Meta:
        model = PreviousTrips
        fields = ['content']

class UserProfileSerializer(ModelSerializer):
    bookmarked = BookmarkedSerializer(many=True, read_only=True)
    previous_trips = PreviousTripsSerializer(many=True, read_only=True)

    profile_image = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'intro', 'trip_type', 'profile_image', 'bookmarked', 'previous_trips']

    def get_profile_image(self, obj):
        if obj.profile_image:
            return f"{settings.MEDIA_URL}{obj.profile_image}"
        return None