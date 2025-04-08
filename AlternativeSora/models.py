from django.db import models

class AlternativeActions_tb(models.Model):
    titleAlternative = models.CharField(max_length = 250, verbose_name = 'Alternative Name')
    descriptionAlternative = models.TextField(verbose_name = 'Description Alternative')
    
class MediaAlternative_tb(models.Model):
    linkAlternative = models.TextField(verbose_name = 'Link Spotify Alternative')
    alternativeAction = models.ForeignKey(AlternativeActions_tb, on_delete = models.CASCADE)