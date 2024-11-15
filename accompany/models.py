from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Accompany(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    trip_type = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField()
    travel_area = models.CharField(max_length=100)
    travel_period = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    accompany = models.ForeignKey(Accompany, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)
    anonymous_name = models.CharField(max_length=20, editable=False)
    def save(self, *args, **kwargs):
        if not self.id:
            # 해당 Accompany의 기존 댓글 수를 세서 익명 이름을 지정
            existing_comments = Comment.objects.filter(accompany=self.accompany).count() + 1
            self.anonymous_name = f"익명{existing_comments}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.anonymous_name}: {self.content[:20]}"