from django.urls import path, include
from rest_framework import routers
from UserSora.views import UserViewSet, CreateUserView, CustomTokenObtain, send_magic_link, reset_password
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

routerUser = routers.DefaultRouter()
routerUser.register(r'user', UserViewSet)

urlpatterns = [
    path('user/', include(routerUser.urls)),
    path('register/',CreateUserView.as_view(), name = 'register'),
    path('token/', TokenObtainPairView.as_view(serializer_class = CustomTokenObtain), name = 'Token'),
    path('token/refresh/', TokenRefreshView.as_view(), name = 'Refresh'),    
    path('sendForgotPassword/', send_magic_link, name = 'Forgot'),
    path('resetPassword/<str:token>/', reset_password, name = 'reset_password')
]