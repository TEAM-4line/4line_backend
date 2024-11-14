from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
class Test(models.Model):
    id = models.AutoField(primary_key=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Travel Style
    TRAVEL_STYLE_CHOICES = [
        ('early_bird', '아침 일찍 일출 보고\n조식까지 야무지게 먹어줌'),
        ('late_riser', '아침은 푹 쉬다가\n체크아웃 시각에 맞춰서 나가자!'),
        ('relaxed_checkout', '조식 먹고 조금 쉬다가\n여유롭게 체크아웃 GOGO')
    ]
    travel_style = models.CharField(max_length=20, choices=TRAVEL_STYLE_CHOICES)

    # Transportation
    TRANSPORTATION_CHOICES = [
        ('public_transport', '운전은 피곤해.\n대중교통 타고 가자'),
        ('drive', '차가 있어야 편하지!\n운전해서 가자')
    ]
    transportation = models.CharField(max_length=20, choices=TRANSPORTATION_CHOICES)

    # Cafe Wait Time
    CAFE_WAIT_CHOICES = [
        ('wait', '웨이팅이 있는 이유가 있음..\n기다린다'),
        ('skip', '장난하시나요? 굳이? 다른 곳 감'),
        ('find_alternative', '근처에 비슷한 예쁜 카페\n찾아서 GOGO')
    ]
    cafe_wait_time = models.CharField(max_length=20, choices=CAFE_WAIT_CHOICES)

    # Luggage Amount
    LUGGAGE_CHOICES = [
        ('minimal', '없으면 가서 사면 돼!\n최대한 간소하게 챙기자'),
        ('essential', '꼭 필요한 것은 다 챙겨야지\n실속 있게 챙기자'),
        ('everything', '혹시 필요할지도 모르니까,\n이것도 저것도 다 챙겨야지')
    ]
    luggage_amount = models.CharField(max_length=20, choices=LUGGAGE_CHOICES)

    # Route Preference
    ROUTE_CHOICES = [
        ('city', '시끌벅적 구경할 것 많은 도시로'),
        ('nature', '공기 좋고 마음 편한 자연 속으로')
    ]
    route_preference = models.CharField(max_length=20, choices=ROUTE_CHOICES)

    # Sea Discovery
    SEA_DISCOVERY_CHOICES = [
        ('play_now', '당장 주자해;;;\n여기서 놀자'),
        ('save_for_later', '다음에 꼭 와야지!\n지도에 저장한다'),
        ('rearrange_schedule', '남은 시간 중에 다시 올 수 있나?\n일정을 정리해본다')
    ]
    sea_discovery = models.CharField(max_length=20, choices=SEA_DISCOVERY_CHOICES)

    # Dinner Choice
    DINNER_CHOICES = [
        ('famous_restaurant', '이 지역에서 가장 유명한\n줄서는 식당'),
        ('local_recommendation', '현지인들이 추천하는\n로컬 식당'),
        ('unique_spot', '걷다가 만난 독특한 외관의 식당')
    ]
    dinner_choice = models.CharField(max_length=20, choices=DINNER_CHOICES)

    # First Stop
    FIRST_STOP_CHOICES = [
        ('activity_place', '재밌는 활동을 할 수 있는 곳'),
        ('rest_place', '조용히 휴식을 취할 수 있는 곳')
    ]
    first_stop = models.CharField(max_length=20, choices=FIRST_STOP_CHOICES)

    # Budget Approach
    BUDGET_CHOICES = [
        ('spend_more', '돈 좀 더 걷으면 되지 ㅋㅋ\n공금으로 10만원 결제'),
        ('strict_budget', '야 이거 먹으면 공금 초과야...\n예산 절대 못 넘기게 함'),
        ('save_for_later', '이거 살 바에 그냥 아껴서\n나중에 공금 뿜빠이 하자...')
    ]
    budget_approach = models.CharField(max_length=20, choices=BUDGET_CHOICES)

    # Trip Planning Style
    PLANNING_STYLE_CHOICES = [
        ('minimal', '숙소랑 비행기 예약하면 끝!\n나머지는 그때 가서 생각하지 뭐 ㅋ'),
        ('basic_plan', '꼭 필요한 예약이랑\n가고 싶은 곳 정도는 정리해 둘까?'),
        ('detailed_plan', '휴가를 망칠 수 없지!\n엑셀에 분 단위로 계획 세움')
    ]
    trip_planning_style = models.CharField(max_length=20, choices=PLANNING_STYLE_CHOICES)
