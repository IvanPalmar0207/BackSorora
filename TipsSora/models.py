from django.db import models

# Create your models here.

class Tips(models.Model):
    nameTip = models.CharField(max_length = 150, verbose_name = 'Tip Name')
    imageTip = models.ImageField(upload_to = 'media')    
    descriptionTip = models.TextField(verbose_name = 'Description Field')
    goodSituation = models.TextField(verbose_name = 'Good Situation')
    badSituation = models.TextField(verbose_name = 'Bad Situation')