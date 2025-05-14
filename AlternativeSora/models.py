from django.db import models

class AlternativeActions_tb(models.Model):
    titleAlternative = models.CharField(max_length = 250, verbose_name = 'Alternative Name')
    descriptionAlternative = models.TextField(verbose_name = 'Description Alternative')
    
class MediaAlternative_tb(models.Model):
    nameAlternative = models.CharField(max_length = 250, verbose_name = 'Name Alternative')
    linkAlternative = models.TextField(verbose_name = 'Link Alternative')
    alternativeAction = models.ForeignKey(AlternativeActions_tb, on_delete = models.CASCADE)