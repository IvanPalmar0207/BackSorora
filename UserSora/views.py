from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .serializer import UserSerializer
from .models import User
from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import User, ageUser_tb, educationLevelUser_tb, relationKindUser_tb, workUser_tb, rangeSalary_tb
from .serializer import AgeUserSerializer, EducationUserSerializer, RelationUserSerializer, WorkUserSerializer, SalaryUserSerializer

#Age Views
class AgeUserViewSet(viewsets.ModelViewSet):
    queryset = ageUser_tb.objects.all()
    serializer_class = AgeUserSerializer
    permission_classes = [IsAuthenticated]
    
    @classmethod
    def get_extra_actions(cls):
        return []
    
#Education Views
class EducationUserViewSet(viewsets.ModelViewSet):
    queryset = educationLevelUser_tb.objects.all()
    serializer_class = EducationUserSerializer
    permission_classes = [IsAuthenticated]

    @classmethod
    def get_extra_actions(cls):
        return []
    
#Relation Views
class RelationUserViewSet(viewsets.ModelViewSet):
    queryset = relationKindUser_tb.objects.all()
    serializer_class = RelationUserSerializer
    permission_classes = [IsAuthenticated]
    
    @classmethod
    def get_extra_actions(cls):
        return []

#Work Views
class WorkUserViewSet(viewsets.ModelViewSet):
    queryset = workUser_tb.objects.all()
    serializer_class = WorkUserSerializer
    permission_classes = [IsAuthenticated]
    
    @classmethod
    def get_extra_actions(cls):
        return []

#Salary Views
class SalaryUserViewSet(viewsets.ModelViewSet):
    queryset = rangeSalary_tb.objects.all()
    serializer_class = SalaryUserSerializer
    permission_classes = [IsAuthenticated]
    
    @classmethod
    def get_extra_actions(cls):
        return []

#User Views
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
#Token Views
class CustomTokenObtain(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        token['is_admin'] = user.is_superuser
        token['email'] = user.email
        return token
        
#Password Reset forgot
signer = TimestampSigner() #Sign unique data
@api_view(['POST']) #Type view define
@permission_classes([AllowAny]) #Permission classes for this view
def send_magic_link(request):    
    email = request.data.get('email') #Get email user
    
    try:
        user = User.objects.get(email = email) #Finduser or error
    except User.DoesNotExist:
        return Response({'message' : 'El correo no existe, intenta nuevamente.'}, status = 404)    
    
    token = signer.sign(user.id) #Generate a secure token with the user id
    magic_link = f'https://sorora.areandina.edu.co/confirmPassword/{token}'
    
    send_mail(
        'Recuperación de contraseña',
        f'Haz click en el enlace para poder restablecer tu contraseña: {magic_link}',
        'noreply@sorora.com',
        [email]
    )
    
    return Response({'message' : 'Se ha enviado un mensaje a tu correo electronico, comprueba.'}, status = 200)    

#Reset Password
@api_view(['POST'])
@permission_classes([AllowAny])
def reset_password(request, token):
    try:
        userId = signer.unsign(token, max_age = 3600)
        user = User.objects.get(id = userId)
    except(BadSignature, SignatureExpired):
        return Response({'message' : 'El enlace ya no es valido, intenta nuevamente.'}, status = 400)
    
    newPassword = request.data.get('password')
    user.set_password(newPassword)
    user.save()
    
    return Response({'message' : 'La contraseña ha sido restablecida correctamente.'}, status = 200)