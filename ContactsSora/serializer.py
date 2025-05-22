from rest_framework import serializers
from .models import AttentionRoute_tb, categoryAR_tb, userContactConfidence_tb

class ARSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttentionRoute_tb
        fields = ['id', 'titleCat', 'whatsappAR', 'phoneAR', 'locationAR']         
        
class arCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = categoryAR_tb
        fields = '__all__'
        
class userContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = userContactConfidence_tb
        fields = '__all__'