from django.db import models
from UserSora.models import User

class categoryAR_tb(models.Model):
    titleCat = models.CharField(max_length = 150, verbose_name = 'Title Net')

class AttentionRoute_tb(models.Model):    
    whatsappAR = models.CharField(max_length = 30, verbose_name = 'Whatsapp AR', null = True)
    phoneAR = models.CharField(max_length = 35, null = True , verbose_name = 'Phone AR')
    locationAR = models.CharField(max_length = 250, null = True, verbose_name = 'Location AR')
    titleCat = models.ForeignKey(categoryAR_tb, on_delete = models.CASCADE)    
    
class userContactConfidence_tb(models.Model):
    nameContact = models.CharField(max_length = 250, verbose_name = 'Name Contact')
    numberContact = models.CharField(max_length = 11, verbose_name = 'Contact Number')
    ownerUser = models.ForeignKey(User, on_delete = models.CASCADE)