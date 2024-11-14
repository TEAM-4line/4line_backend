from rest_framework.serializers import ModelSerializer
from .models import User, Bookmarked, PreviousTrips

class UserSerializer(ModelSerializer):
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

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'intro', 'trip_type', 'profile_image', 'bookmarked', 'previous_trips']
