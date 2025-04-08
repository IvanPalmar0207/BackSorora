from django.urls import path, include
from rest_framework import routers 
from .views import PodcastViewSet, PodcastViewSetUser

routerPodcast = routers.DefaultRouter()
routerPodcast.register(r'podcast', PodcastViewSet)

urlpatterns = [
    path('podcast/', include(routerPodcast.urls)),
    path('podcastUser/', PodcastViewSetUser.as_view()),
]