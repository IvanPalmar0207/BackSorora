from rest_framework import serializers
from .models import AlternativeActions_tb, MediaAlternative_tb

class AlternativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlternativeActions_tb
        fields = '__all__'
    
class MediaAlternativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaAlternative_tb
        fields = '__all__'