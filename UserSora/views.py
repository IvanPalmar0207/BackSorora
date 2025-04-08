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
    magic_link = f'http://localhost:5173/confirmPassword/{token}'
    
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