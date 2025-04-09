from rest_framework import serializers, generics
from .models import User, ageUser_tb, educationLevelUser_tb, relationKindUser_tb, workUser_tb, rangeSalary_tb

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'        
        
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

class AgeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ageUser_tb
        fields = '__all__'    
        
class EducationUserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = educationLevelUser_tb
        fields = '__all__'
        
class RelationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = relationKindUser_tb
        fields = '__all__'
        
class WorkUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = workUser_tb
        fields = '__all__'
    
class SalaryUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = rangeSalary_tb
        fields = '__all__'