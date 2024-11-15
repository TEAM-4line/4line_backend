from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny
'''

'''
class TestViewSet(viewsets.ModelViewSet):
    
    queryset = Test.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'list':
            return TestListSerializer
        elif self.action == 'retrieve':
            return TestSerializer
        return TestListSerializer
