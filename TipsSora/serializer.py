from rest_framework import serializers
from .models import Tips

class TipsSerializer(serializers.ModelSerializer):
    imageTip = serializers.ImageField(use_url = True)
    class Meta:
        model = Tips
        fields = '__all__'