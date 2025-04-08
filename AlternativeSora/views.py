from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializer import AlternativeSerializer, MediaAlternativeSerializer 
from .models import AlternativeActions_tb, MediaAlternative_tb

#AlternativeActions
class AlternativeViewSet(viewsets.ModelViewSet):
    queryset = AlternativeActions_tb.objects.all()
    serializer_class = AlternativeSerializer
    permission_classes = [IsAuthenticated]
    
#AlternativeActions User
class AlternativeUserViewSet(generics.ListAPIView):
    queryset = AlternativeActions_tb.objects.all()
    serializer_class = AlternativeSerializer
    permission_classes = [AllowAny]
    
#Alternative One
class AlternativeOneUserViewSet(generics.RetrieveAPIView):
    queryset = AlternativeActions_tb.objects.all()
    serializer_class = AlternativeSerializer
    permission_classes = [AllowAny]
    
#MediaAlternative
class MediaAlternativeViewSet(viewsets.ModelViewSet):    
    serializer_class = MediaAlternativeSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        alternativeId = self.request.query_params.get('id')
        return MediaAlternative_tb.objects.filter(alternativeAction = alternativeId)
    
#MediaAlternative User
class MediaAlternativeUserViewSet(generics.ListAPIView):
    serializer_class = MediaAlternativeSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        alternativeId = self.request.query_params.get('id')
        return MediaAlternative_tb.objects.filter(alternativeAction = alternativeId)