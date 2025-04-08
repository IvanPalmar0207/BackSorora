from django.db import models

class Exam_tb(models.Model):
    titleExam = models.CharField(max_length = 250, verbose_name = 'Exam Name')
    
class Questions_tb(models.Model):
    nameQuestion = models.TextField(verbose_name = 'Question Name')
    scoreQuestion = models.IntegerField(verbose_name = 'Question Score')
    examBelong = models.ForeignKey(Exam_tb, on_delete = models.CASCADE)    
    
class ScoreExam_tb(models.Model):
    minScore = models.IntegerField(verbose_name = 'Min Score')
    maxScore = models.IntegerField(verbose_name = 'Max Score')
    violenceType = models.CharField(blank = True ,max_length = 250, verbose_name = 'Violence Type')
    messageScore = models.TextField(verbose_name = 'Message Score')
    idExam = models.ForeignKey(Exam_tb, on_delete = models.CASCADE,verbose_name = 'Exam')   
    
class ActionScore_tb(models.Model):
    linkAction = models.CharField(max_length = 255, verbose_name = 'Link Action')
    nameAction = models.CharField(max_length = 255, verbose_name = 'Link Action')
    idScore = models.ForeignKey(ScoreExam_tb, on_delete = models.CASCADE)