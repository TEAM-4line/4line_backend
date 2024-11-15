from django.forms import ValidationError
from rest_framework import serializers
from .models import *
from users.models import User


class TestListSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()
    def get_name(self, obj):
        # writer 필드에서 사용자 이름을 가져옴
        return obj.name.name
    
    def create(self, validated_data):
        # `name` 필드를 요청한 사용자로 설정
        user = self.context['request'].user
        if user.is_anonymous:
            raise serializers.ValidationError("인증된 사용자가 필요합니다.")

        validated_data['name'] = user

        # 인스턴스를 먼저 생성
        instance = Test.objects.create(**validated_data)

        # `trip_type` 계산 후 저장
        trip_type = self.get_trip_type(instance)
        instance.trip_type = trip_type
        instance.save()

        return instance
    
    def get_trip_type(self, instance):
        # 각 타입별 초기 점수
        lion = 0
        owl = 0
        monkey = 0
        cat = 0
        dolphin = 0
        fox = 0

        # travel_style 점수 계산
        if instance.travel_style == 'early_bird':
            owl += 14
        elif instance.travel_style == 'late_riser':
            cat += 14
        elif instance.travel_style == 'relaxed_checkout':
            monkey += 14

        # transportation 점수 계산
        if instance.transportation == 'public_transport':
            fox += 10
        elif instance.transportation == 'drive':
            lion += 10

        # cafe_wait_time 점수 계산
        if instance.cafe_wait_time == 'wait':
            fox += 10
        elif instance.cafe_wait_time == 'skip':
            monkey += 10
        elif instance.cafe_wait_time == 'find_alternative':
            dolphin += 10

        # luggage_amount 점수 계산
        if instance.luggage_amount == 'minimal':
            monkey += 11
        elif instance.luggage_amount == 'essential':
            owl += 11
        elif instance.luggage_amount == 'everything':
            cat += 11

        # route_preference 점수 계산
        if instance.route_preference == 'city':
            dolphin += 13
        elif instance.route_preference == 'nature':
            cat += 13

        # sea_discovery 점수 계산
        if instance.sea_discovery == 'play_now':
            monkey += 11
        elif instance.sea_discovery == 'save_for_later':
            lion += 11
        elif instance.sea_discovery == 'rearrange_schedule':
            owl += 11

        # dinner_choice 점수 계산
        if instance.dinner_choice == 'famous_restaurant':
            fox += 14
        elif instance.dinner_choice == 'local_recommendation':
            dolphin += 14
        elif instance.dinner_choice == 'unique_spot':
            lion += 14

        # first_stop 점수 계산
        if instance.first_stop == 'activity_place':
            lion += 13
        elif instance.first_stop == 'rest_place':
            cat += 13

        # budget_approach 점수 계산
        if instance.budget_approach == 'spend_more':
            lion += 10
        elif instance.budget_approach == 'strict_budget':
            owl += 10
        elif instance.budget_approach == 'save_for_later':
            dolphin += 10

        # trip_planning_style 점수 계산
        if instance.trip_planning_style == 'minimal':
            monkey += 15
        elif instance.trip_planning_style == 'basic_plan':
            fox += 15
        elif instance.trip_planning_style == 'detailed_plan':
            owl += 15

        # 각 동물별 점수를 딕셔너리로 반환하여 가장 높은 점수를 가진 동물 선택
        animal_scores = {
            'lion': lion,
            'owl': owl,
            'monkey': monkey,
            'cat': cat,
            'dolphin': dolphin,
            'fox': fox
        }
        top_animal = max(animal_scores, key=animal_scores.get)
        return top_animal

        return instance
    class Meta:
        model = Test
        fields = ['id', 'name', 'travel_style', 'transportation', 'cafe_wait_time', 
                'luggage_amount', 'route_preference', 'sea_discovery', 'dinner_choice', 
                'first_stop', 'budget_approach', 'trip_planning_style']

class TestSerializer(serializers.ModelSerializer):
    trip_type = serializers.SerializerMethodField()  # type 필드 추가
    name = serializers.SerializerMethodField()
    def get_name(self, obj):
        # writer 필드에서 사용자 이름을 가져옴
        return obj.name.name

    def get_trip_type(self, instance):
        # 각 타입별 초기 점수
        lion = 0
        owl = 0
        monkey = 0
        cat = 0
        dolphin = 0
        fox = 0

        # travel_style 점수 계산
        if instance.travel_style == 'early_bird':
            owl += 14
        elif instance.travel_style == 'late_riser':
            cat += 14
        elif instance.travel_style == 'relaxed_checkout':
            monkey += 14

        # transportation 점수 계산
        if instance.transportation == 'public_transport':
            fox += 10
        elif instance.transportation == 'drive':
            lion += 10

        # cafe_wait_time 점수 계산
        if instance.cafe_wait_time == 'wait':
            fox += 10
        elif instance.cafe_wait_time == 'skip':
            monkey += 10
        elif instance.cafe_wait_time == 'find_alternative':
            dolphin += 10

        # luggage_amount 점수 계산
        if instance.luggage_amount == 'minimal':
            monkey += 11
        elif instance.luggage_amount == 'essential':
            owl += 11
        elif instance.luggage_amount == 'everything':
            cat += 11

        # route_preference 점수 계산
        if instance.route_preference == 'city':
            dolphin += 13
        elif instance.route_preference == 'nature':
            cat += 13

        # sea_discovery 점수 계산
        if instance.sea_discovery == 'play_now':
            monkey += 11
        elif instance.sea_discovery == 'save_for_later':
            lion += 11
        elif instance.sea_discovery == 'rearrange_schedule':
            owl += 11

        # dinner_choice 점수 계산
        if instance.dinner_choice == 'famous_restaurant':
            fox += 14
        elif instance.dinner_choice == 'local_recommendation':
            dolphin += 14
        elif instance.dinner_choice == 'unique_spot':
            lion += 14

        # first_stop 점수 계산
        if instance.first_stop == 'activity_place':
            lion += 13
        elif instance.first_stop == 'rest_place':
            cat += 13

        # budget_approach 점수 계산
        if instance.budget_approach == 'spend_more':
            lion += 10
        elif instance.budget_approach == 'strict_budget':
            owl += 10
        elif instance.budget_approach == 'save_for_later':
            dolphin += 10

        # trip_planning_style 점수 계산
        if instance.trip_planning_style == 'minimal':
            monkey += 15
        elif instance.trip_planning_style == 'basic_plan':
            fox += 15
        elif instance.trip_planning_style == 'detailed_plan':
            owl += 15

        # 각 동물별 점수를 딕셔너리로 반환하여 가장 높은 점수를 가진 동물 선택
        animal_scores = {
            'lion': lion,
            'owl': owl,
            'monkey': monkey,
            'cat': cat,
            'dolphin': dolphin,
            'fox': fox
        }
        top_animal = max(animal_scores, key=animal_scores.get)
        return top_animal
    class Meta:
        model = Test
        fields = ['id', 'trip_type', 'name']