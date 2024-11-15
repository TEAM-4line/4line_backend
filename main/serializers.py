# serializers.py
from rest_framework import serializers
from users.models import User
from community.models import Community  # Community 모델 임포트
from question.models import Test
from django.contrib.auth.models import AnonymousUser
class MainUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    
    trip_type = serializers.SerializerMethodField()
    type_content = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['name', 'trip_type','type_content']
    
    def get_name(self, obj):
        return getattr(obj, 'name', '')
    
    def get_trip_type(self, obj):
        # 사용자의 최근 테스트 결과에서 trip_type 가져오기
        if isinstance(obj, AnonymousUser):
            return None
        
        latest_test = Test.objects.filter(name=obj).order_by('-id').first()
        return latest_test.trip_type if latest_test else obj.trip_type
    
    def get_type_content(self, obj):
        if isinstance(obj, AnonymousUser):
            return '기타'
        # trip_type에 따른 type_content 설정
        trip_type_content_mapping = {
            'lion': '용맹한 모험가,',
            'owl': '섬세한 계획자,',
            'monkey': '즉흥적인 자유인,',
            'cat': '편안한 휴식가,',
            'dolphin': '사교적인 리더,',
            'fox': '호기심 많은 탐험가,'
        }
        trip_type = self.get_trip_type(obj)
        return trip_type_content_mapping.get(trip_type, '기타')

class PopularCommunitySerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(read_only=True)  # source 제거
    scrap_count = serializers.IntegerField(read_only=True)  # source 제거

    class Meta:
        model = Community
        fields = ['id', 'region', 'title','like_count','scrap_count','photo']