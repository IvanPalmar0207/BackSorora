from rest_framework import serializers
from .models import podcastMedia_tb

class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = podcastMedia_tb
        fields = '__all__'