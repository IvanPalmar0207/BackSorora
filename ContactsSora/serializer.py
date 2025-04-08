from rest_framework import serializers
from .models import AttentionRoute_tb, categoryAR_tb

class ARSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttentionRoute_tb
        fields = ['id', 'titleCat', 'whatsappAR', 'phoneAR', 'locationAR']         
        
class arCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = categoryAR_tb
        fields = '__all__'