from django.urls import path, include
from rest_framework import routers
from .views import TipsViewSet, TipsViewUser, TipGetOneUser

routerTips = routers.DefaultRouter()
routerTips.register(r'tips', TipsViewSet)

urlpatterns = [
    path('tips/', include(routerTips.urls)),
    path('tipsAll/', TipsViewUser.as_view()),
    path('oneTipUser/<int:pk>/', TipGetOneUser.as_view())
]