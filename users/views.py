from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, logout as auth_logout
from .models import User
from .serializers import UserSerializer, UserProfileSerializer
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
import random

# class SignUpView(APIView):
#     def post(self, request):
#         name = request.data.get('name')
#         birth = request.data.get('birth')
#         password = request.data.get('password')
#         password2 = request.data.get('password2')
#         email = request.data.get('email')
#         intro = request.data.get('intro')

#         # 비밀번호 일치 확인
#         if password != password2:
#             return Response({"message": "입력한 비밀번호가 다릅니다."}, status=status.HTTP_400_BAD_REQUEST)
        
#         # 비밀번호 유효성 검사
#         try:
#             validate_password(password)
#         except ValidationError as e:
#             return Response({"message": e.messages}, status=status.HTTP_400_BAD_REQUEST)

#         # serializer로 유효성 검사 후 데이터 전달
#         data = {
#             "name": name,
#             "birth": birth,
#             "email": email,
#             "password": password,
#             "intro": intro
#         }
#         serializer = UserSerializer(data=data)
        
#         # 데이터 유효성 검사 및 저장
#         if serializer.is_valid(raise_exception=True):
#             user = serializer.save()
#             user.set_password(password)  # 비밀번호 암호화 저장
#             user.save()

#             return Response({"message": "회원가입에 성공하였습니다."}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
         
class SignUpView(APIView):
    def post(self, request):
        name = request.data.get('name')
        birth = request.data.get('birth')
        password = request.data.get('password')
        password2 = request.data.get('password2')
        email = request.data.get('email')
        intro = request.data.get('intro')

        # 비밀번호 일치 확인
        if password != password2:
            return Response({"message": "입력한 비밀번호가 다릅니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        # 비밀번호 유효성 검사
        try:
            validate_password(password)
        except ValidationError as e:
            return Response({"message": e.messages}, status=status.HTTP_400_BAD_REQUEST)

        # 랜덤 프로필 이미지 선택
        image_list = [
            "profile1.png",
            "profile2.png",
            "profile3.png",
            "profile4.png",
            "profile5.png",
            "profile6.png",
            "profile7.png",
            "profile8.png",
        ]
        random_image = random.choice(image_list)

        # serializer로 유효성 검사 후 데이터 전달
        data = {
            "name": name,
            "birth": birth,
            "email": email,
            "password": password,
            "intro": intro,
            "profile_image": random_image  # 랜덤 이미지 배정
        }
        serializer = UserSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user.set_password(password)  # 비밀번호 암호화 저장
            user.save()

            return Response({"id": user.id, "message": "회원가입에 성공하였습니다."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
# 로그인 뷰
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            return Response({
                "id": user.id,
                "trip_type": user.trip_type,
                "message": "로그인 성공"
            }, status=status.HTTP_200_OK)
        return Response({"message": "로그인 실패"}, status=status.HTTP_400_BAD_REQUEST)
    
# 탈퇴 뷰
class QuitView(APIView):
    def delete(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            user.delete()
            auth_logout(request) 
            return Response({"message": "탈퇴에 성공하였습니다. "}, status = status.HTTP_200_OK)
        else:
            return Response({"message": "이름 혹은 비밀번호가 잘못 입력 되었습니다. "}, status = status.HTTP_401_UNAUTHORIZED)

class ProfileView(APIView):
    # 프로필 조회
    def get(self, request):
        name = request.GET.get('name')
        
        if name:
            # 특정 유저 정보 조회
            user = get_object_or_404(User, name=name)
            serializer = UserProfileSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            # 모든 유저 정보 조회
            users = User.objects.all()
            serializer = UserProfileSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
