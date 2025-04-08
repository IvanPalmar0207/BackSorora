from django.urls import path, include
from rest_framework import routers
from .views import TestViewSet, TestViewSetUser, CatTestViewSet, TestOneUser

routerTest = routers.DefaultRouter()
routerTest.register(r'test', TestViewSet)

urlpatterns = [
    path('test/', include(routerTest.urls)),
    path('testAll/', TestViewSetUser.as_view()),
    path('catTest/', CatTestViewSet.as_view()),
    path('testOneUser/<int:pk>', TestOneUser.as_view())
]