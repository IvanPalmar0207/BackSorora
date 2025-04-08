from rest_framework import serializers
from .models import Exam_tb, Questions_tb, ScoreExam_tb, ActionScore_tb

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam_tb
        fields = '__all__'
        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions_tb
        fields = '__all__'
        
class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreExam_tb
        fields = '__all__'
        
class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionScore_tb
        fields = '__all__'