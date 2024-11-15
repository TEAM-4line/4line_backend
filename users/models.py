from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수입니다.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        #추후에 삭제
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        #여기까지
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    name = models.CharField(max_length=30)
    birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    intro = models.CharField(max_length=100, blank=True)
    trip_type = models.CharField(max_length=20, choices=[
        ('lion', '사자'),
        ('owl', '부엉이'),
        ('monkey', '원숭이'),
        ('dolphin', '돌고래'),
        ('fox', '여우'),
        ('cat', '고양이')
    ], null=True, blank=True)
    profile_image = models.CharField(max_length=255, blank=True, null=True)  # 프로필 이미지 필드 추가

    is_staff = models.BooleanField(default=False)  # 추후에 삭제
    is_superuser = models.BooleanField(default=False) #추후에 삭제

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    
class Bookmarked(models.Model):
    user = models.ForeignKey(User, related_name="bookmarked", on_delete=models.CASCADE)
    content = models.TextField()  # 스크랩한 글 내용

class PreviousTrips(models.Model):
    user = models.ForeignKey(User, related_name="previous_trips", on_delete=models.CASCADE)
    content = models.TextField()  # 사용자가 작성했던 글 내용

