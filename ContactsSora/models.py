from django.db import models

class categoryAR_tb(models.Model):
    titleCat = models.CharField(max_length = 150, verbose_name = 'Title Net')

class AttentionRoute_tb(models.Model):    
    whatsappAR = models.CharField(max_length = 30, verbose_name = 'Whatsapp AR', null = True)
    phoneAR = models.CharField(max_length = 35, null = True , verbose_name = 'Phone AR')
    locationAR = models.CharField(max_length = 250, null = True, verbose_name = 'Location AR')
    titleCat = models.ForeignKey(categoryAR_tb, on_delete = models.CASCADE)    