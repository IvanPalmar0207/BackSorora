from django.urls import path, include
from rest_framework import routers
from UserSora.views import UserViewSet, CreateUserView, CustomTokenObtain, send_magic_link, reset_password, AgeUserViewSet, EducationUserViewSet, RelationUserViewSet, WorkUserViewSet, SalaryUserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

routerUser = routers.DefaultRouter()
routerUser.register(r'user', UserViewSet, basename = 'User')

routerAge = routers.DefaultRouter()
routerAge.register(r'ageUser', AgeUserViewSet, basename = 'ageUser')

routerEducation = routers.DefaultRouter()
routerEducation.register(r'educationUser', EducationUserViewSet, basename = 'educationUser')

routerRelation = routers.DefaultRouter()
routerRelation.register(r'relationUser', RelationUserViewSet, basename = 'relationUser')

routerWork = routers.DefaultRouter()
routerWork.register(r'workUser', WorkUserViewSet, basename = 'workUser')

routerSalary = routers.DefaultRouter()
routerSalary.register(r'salaryUser', SalaryUserViewSet, basename = 'salaryUser')


urlpatterns = [
    path('user/', include(routerUser.urls)),
    path('register/',CreateUserView.as_view(), name = 'register'),
    path('token/', TokenObtainPairView.as_view(serializer_class = CustomTokenObtain), name = 'Token'),
    path('token/refresh/', TokenRefreshView.as_view(), name = 'Refresh'),    
    path('sendForgotPassword/', send_magic_link, name = 'Forgot'),
    path('resetPassword/<str:token>/', reset_password, name = 'reset_password'),
    
    path('ageUser/', include(routerAge.urls)),
    path('educationUser/', include(routerEducation.urls)),
    path('relationUser/', include(routerRelation.urls)),
    path('workUser/', include(routerWork.urls)),
    path('salaryUser/', include(routerSalary.urls))
]