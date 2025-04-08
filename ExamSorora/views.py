from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializer import ExamSerializer, QuestionSerializer, ScoreSerializer, ActionSerializer
from .models import Exam_tb, Questions_tb, ScoreExam_tb, ActionScore_tb

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam_tb.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [IsAuthenticated]
    
class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        examId = self.request.query_params.get('id')
        return Questions_tb.objects.filter(examBelong = examId)

class ScoreViewSet(viewsets.ModelViewSet):
    serializer_class = ScoreSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        examId = self.request.query_params.get('id')
        return ScoreExam_tb.objects.filter(idExam = examId)
    
class ActionViewSet(viewsets.ModelViewSet):
    serializer_class = ActionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        idScores = self.request.query_params.get('id')
        return ActionScore_tb.objects.filter(idScore = idScores)