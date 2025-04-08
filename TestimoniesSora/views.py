from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializer import TestSerializer, catTestSerializer
from .models import testimonies_tb, categoryTestimonie_tb

#Cat Testimonies
class CatTestViewSet(generics.ListAPIView):
    queryset = categoryTestimonie_tb.objects.all()
    serializer_class = catTestSerializer
    permission_classes = [AllowAny]

#Testimonies Routes
class TestViewSet(viewsets.ModelViewSet):
    queryset = testimonies_tb.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]
    
class TestViewSetUser(generics.ListAPIView):    
    serializer_class = TestSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        categoryId = self.request.query_params.get('id')
        return testimonies_tb.objects.filter(catTest = categoryId)
    
class TestOneUser(generics.RetrieveAPIView):
    queryset = testimonies_tb.objects.all()
    serializer_class = TestSerializer
    permission_classes = [AllowAny]