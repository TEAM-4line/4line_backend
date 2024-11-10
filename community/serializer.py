from rest_framework import serializers
from .models import *

class CommunitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Community
        frield = '__all__'