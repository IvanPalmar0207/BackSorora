from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializer import PodcastSerializer
from .models import podcastMedia_tb

#Podcast View
class PodcastViewSet(viewsets.ModelViewSet):
    queryset = podcastMedia_tb.objects.all()
    serializer_class = PodcastSerializer
    permission_classes = [IsAuthenticated]
#Podcast User 
class PodcastViewSetUser(generics.ListAPIView):
    queryset = podcastMedia_tb.objects.all()
    serializer_class = PodcastSerializer
    permission_classes = [AllowAny]