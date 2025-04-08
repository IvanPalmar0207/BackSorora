from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializer import ARSerializer, arCategorySerializer
from .models import AttentionRoute_tb, categoryAR_tb

#Attention Routes Views
class ARViewSet(viewsets.ModelViewSet):
    queryset = AttentionRoute_tb.objects.all()
    serializer_class = ARSerializer
    permission_classes = [IsAuthenticated]
    
class ARViewSetUser(generics.ListAPIView):
    queryset = AttentionRoute_tb.objects.all()
    serializer_class = ARSerializer
    permission_classes = [AllowAny]
    
class CatOneViewSet(generics.ListAPIView):
    serializer_class = ARSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):                
        categoryId = self.request.query_params.get('id')
        return AttentionRoute_tb.objects.filter(titleCat = categoryId)

#CategoryRA Views    
class CatArViewSet(viewsets.ModelViewSet):
    queryset = categoryAR_tb.objects.all()
    serializer_class = arCategorySerializer
    permission_classes = [IsAuthenticated]
    
class CatArViewSetUser(generics.ListAPIView):
    queryset = categoryAR_tb.objects.all()
    serializer_class = arCategorySerializer
    permission_classes = [AllowAny]
    
class CatGetOneView(generics.RetrieveAPIView):
    queryset = categoryAR_tb.objects.all()
    serializer_class = arCategorySerializer
    permission_classes = [AllowAny]