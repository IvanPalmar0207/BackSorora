from django.urls import path, include
from rest_framework import routers
from .views import ARViewSet, ARViewSetUser, CatArViewSet, CatArViewSetUser, CatOneViewSet, CatGetOneView, UserContactView

routerAR = routers.DefaultRouter()
routerAR.register(r'AR', ARViewSet, basename = 'Ar Router')

routerCat = routers.DefaultRouter()
routerCat.register(r'catAr', CatArViewSet, basename = 'Cat Router')

routerContactUser = routers.DefaultRouter()
routerContactUser.register(r'userCon', UserContactView, basename = 'userCon')

urlpatterns = [
    path('AR/', include(routerAR.urls)),
    path('catAr/', include(routerCat.urls)),
    path('allAR/', ARViewSetUser.as_view()),
    path('allCat/', CatArViewSetUser.as_view()),
    path('allARCat/', CatOneViewSet.as_view()),
    path('getOneCat/<int:pk>', CatGetOneView.as_view()),
    path('userCon/', include(routerContactUser.urls))
]