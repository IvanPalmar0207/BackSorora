from django.db import models
from django_resized import ResizedImageField

# Create your models here.

class Tips(models.Model):
    nameTip = models.CharField(max_length = 150, verbose_name = 'Tip Name')
    imageTip = ResizedImageField(size = [600, 600], quality = 85, upload_to = 'media', verbose_name = 'Image Tip')    
    descriptionTip = models.TextField(verbose_name = 'Description Field')
    goodSituation = models.TextField(verbose_name = 'Good Situation')
    badSituation = models.TextField(verbose_name = 'Bad Situation')