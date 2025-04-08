from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializer import TipsSerializer
from .models import Tips

class TipsViewSet(viewsets.ModelViewSet):
    queryset = Tips.objects.all()
    serializer_class = TipsSerializer
    permission_classes = [IsAuthenticated]

class TipsViewUser(generics.ListAPIView):
    queryset = Tips.objects.all()
    serializer_class = TipsSerializer
    permission_classes = [AllowAny]
    
class TipGetOneUser(generics.RetrieveAPIView):    
    queryset = Tips.objects.all()
    serializer_class = TipsSerializer
    permission_classes = [AllowAny]