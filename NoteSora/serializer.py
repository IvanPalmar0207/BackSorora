from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'titleNote', 'contentNote', 'createdNote', 'isFavorite', 'author']
        extra_kwargs = {'author' : {'read_only' : True}}