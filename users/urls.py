from django.urls import path
from .views import SignUpView, LoginView, ProfileView, QuitView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('quit/', QuitView.as_view(), name='user-quit'),
]
