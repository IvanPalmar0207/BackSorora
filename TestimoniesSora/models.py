from django.db import models

class categoryTestimonie_tb(models.Model):
    categoryTest = models.CharField(max_length = 100, verbose_name = 'Category Testimonies')
    
    def __str__(self):
        return self.categoryTest
    
class testimonies_tb(models.Model):
    authorTest = models.CharField(max_length = 150, verbose_name = 'Author Testimonie')
    descriptionTest = models.TextField(verbose_name = 'Description Testimonie')
    videoTest = models.TextField(verbose_name = 'Video Test')
    articleTest = models.TextField(verbose_name = 'Article Test')
    catTest = models.ForeignKey(categoryTestimonie_tb, default=1, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.authorTest