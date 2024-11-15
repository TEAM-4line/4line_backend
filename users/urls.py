from django.urls import path
from .views import SignUpView, LoginView, ProfileView, QuitView
from .views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView 

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('quit/', QuitView.as_view(), name='user-quit'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # 액세스 및 리프레시 토큰 발급
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # 리프레시 토큰으로 액세스 토큰 갱신
]
