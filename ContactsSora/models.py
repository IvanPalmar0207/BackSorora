from django.db import models
from UserSora.models import User
from django_resized import ResizedImageField

class categoryAR_tb(models.Model):
    nameCat = models.CharField(max_length = 150, verbose_name = 'Title Cat')    
    descriptionCat = models.TextField(verbose_name = 'Description Cat')
    imageCat = ResizedImageField(size = [600, 600], quality = 85, upload_to = 'media', verbose_name = 'Image Cat')
    
class AttentionRoute_tb(models.Model):      
    nameAttention = models.CharField(max_length = 255, verbose_name = 'Name Attention')     
    descriptionAttention = models.TextField(verbose_name = 'Description Attention')
    imageAttention = ResizedImageField(size = [600, 600], quality = 85, upload_to = 'media', verbose_name = 'Image Attention')
    nameCat = models.ForeignKey(categoryAR_tb, on_delete = models.CASCADE)    
    
class userContactConfidence_tb(models.Model):
    nameContact = models.CharField(max_length = 250, verbose_name = 'Name Contact')
    numberContact = models.CharField(max_length = 11, verbose_name = 'Contact Number')
    ownerUser = models.ForeignKey(User, on_delete = models.CASCADE)