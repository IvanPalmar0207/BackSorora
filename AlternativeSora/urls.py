from django.urls import path, include
from rest_framework import routers
from .views import AlternativeViewSet, AlternativeUserViewSet, AlternativeOneUserViewSet, MediaAlternativeViewSet, MediaAlternativeUserViewSet

routerAlternative = routers.DefaultRouter()
routerAlternative.register('alternative', AlternativeViewSet, basename = 'alternative')

routerMediaAlt = routers.DefaultRouter()
routerMediaAlt.register('mediaAlt', MediaAlternativeViewSet, basename = 'mediaAlt')

urlpatterns = [
    path('alternative/', include(routerAlternative.urls)),
    path('alternativeUser/', AlternativeUserViewSet.as_view()),
    path('alternativeOne/<int:pk>', AlternativeOneUserViewSet.as_view()),
    path('mediaAlt/', include(routerMediaAlt.urls)),
    path('mediaAltUser/', MediaAlternativeUserViewSet.as_view()),
]