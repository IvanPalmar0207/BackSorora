from rest_framework import serializers
from .models import testimonies_tb, categoryTestimonie_tb

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = testimonies_tb
        fields = ['id', 'authorTest', 'descriptionTest', 'videoTest', 'articleTest', 'catTest']


class catTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoryTestimonie_tb
        fields = ['id', 'categoryTest']