from django.db import models

class podcastMedia_tb(models.Model):
    linkPodcast = models.TextField(verbose_name = 'Link Podcast')