from rest_framework import serializers, generics
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 
            'email', 
            'password', 
            'age', 
            'educationLevel', 
            'relationKind',
            'haveKids',
            'workSituation', 
            'salaryRange'
        ]
        
        extra_kwargs = {
            'password' : {
                'write_only': True,
            }
        }
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create(email = validated_data['email'])

        user.is_active = True
        
        if password is not None:
            user.set_password(password)
        user.save()
        
        return user
