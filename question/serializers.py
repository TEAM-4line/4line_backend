from rest_framework import serializers
from .models import *


class TestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'
        
class TestSerializer(serializers.ModelSerializer):
    trip_type = serializers.SerializerMethodField()  # type 필드 추가

    class Meta:
        model = Test
        fields = ['id', 'trip_type', 'writer']

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

class TotaltestSerializer(serializers.ModelSerializer):
    writer = serializers.SerializerMethodField(read_only=True)
    test = TestSerializer()
    type = serializers.SerializerMethodField()
    animal_scores = serializers.SerializerMethodField()  # 각 동물 점수를 위한 필드 추가

    # CharField로 변경하고 Test 모델의 choices 설정을 가져오기
    travel_style = serializers.ChoiceField(choices=Test.TRAVEL_STYLE_CHOICES)
    transportation = serializers.ChoiceField(choices=Test.TRANSPORTATION_CHOICES)
    cafe_wait_time = serializers.ChoiceField(choices=Test.CAFE_WAIT_CHOICES)
    luggage_amount = serializers.ChoiceField(choices=Test.LUGGAGE_CHOICES)
    route_preference = serializers.ChoiceField(choices=Test.ROUTE_CHOICES)
    sea_discovery = serializers.ChoiceField(choices=Test.SEA_DISCOVERY_CHOICES)
    dinner_choice = serializers.ChoiceField(choices=Test.DINNER_CHOICES)
    first_stop = serializers.ChoiceField(choices=Test.FIRST_STOP_CHOICES)
    budget_approach = serializers.ChoiceField(choices=Test.BUDGET_CHOICES)
    trip_planning_style = serializers.ChoiceField(choices=Test.PLANNING_STYLE_CHOICES)

    def get_writer(self, instance):
        return instance.writer.username

    def get_type(self, instance):
        animal_scores = self.calculate_animal_scores(instance)
        top_animal = max(animal_scores, key=animal_scores.get)
        return top_animal

    def get_animal_scores(self, instance):
        # 각 동물의 점수 계산 결과를 반환합니다.
        return self.calculate_animal_scores(instance)

    def calculate_animal_scores(self, instance):
        lion = 0
        owl = 0
        monkey = 0
        cat = 0
        dolphin = 0
        fox = 0

        # Travel Style
        if instance.travel_style == 'early_bird':
            owl += 14
        elif instance.travel_style == 'late_riser':
            cat += 14
        elif instance.travel_style == 'relaxed_checkout':
            monkey += 14

        # Transportation
        if instance.transportation == 'public_transport':
            fox += 10
        elif instance.transportation == 'drive':
            lion += 10

        # Cafe Wait Time
        if instance.cafe_wait_time == 'wait':
            fox += 10
        elif instance.cafe_wait_time == 'skip':
            monkey += 10
        elif instance.cafe_wait_time == 'find_alternative':
            dolphin += 10

        # Luggage Amount
        if instance.luggage_amount == 'minimal':
            monkey += 11
        elif instance.luggage_amount == 'essential':
            owl += 11
        elif instance.luggage_amount == 'everything':
            cat += 11

        # Route Preference
        if instance.route_preference == 'city':
            dolphin += 13
        elif instance.route_preference == 'nature':
            cat += 13

        # Sea Discovery
        if instance.sea_discovery == 'play_now':
            monkey += 11
        elif instance.sea_discovery == 'save_for_later':
            lion += 11
        elif instance.sea_discovery == 'rearrange_schedule':
            owl += 11

        # Dinner Choice
        if instance.dinner_choice == 'famous_restaurant':
            fox += 14
        elif instance.dinner_choice == 'local_recommendation':
            dolphin += 14
        elif instance.dinner_choice == 'unique_spot':
            lion += 14

        # First Stop
        if instance.first_stop == 'activity_place':
            lion += 13
        elif instance.first_stop == 'rest_place':
            cat += 13

        # Budget Approach
        if instance.budget_approach == 'spend_more':
            lion += 10
        elif instance.budget_approach == 'strict_budget':
            owl += 10
        elif instance.budget_approach == 'save_for_later':
            dolphin += 10

        # Trip Planning Style
        if instance.trip_planning_style == 'minimal':
            monkey += 15
        elif instance.trip_planning_style == 'basic_plan':
            fox += 15
        elif instance.trip_planning_style == 'detailed_plan':
            owl += 15

        # 각 동물별 점수를 딕셔너리로 반환
        return {
            'lion': lion,
            'owl': owl,
            'monkey': monkey,
            'cat': cat,
            'dolphin': dolphin,
            'fox': fox
        }

    def create(self, validated_data):
        # Totaltest 인스턴스를 생성하고 저장하는 커스텀 로직
        writer = self.context['request'].user
        totaltest = Totaltest.objects.create(writer=writer, **validated_data)
        return totaltest

    class Meta:
        model = Totaltest
        fields = '__all__'


