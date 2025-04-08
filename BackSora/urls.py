from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('UserSora.urls')),
    path('api/', include('TipsSora.urls')),
    path('api/', include('NoteSora.urls')),
    path('api/', include('ContactsSora.urls')),
    path('api/', include('TestimoniesSora.urls')),
    path('api/', include('AlternativeSora.urls')),    
    path('api/', include('PodcastSora.urls')),
    path('api/', include('ExamSorora.urls'))
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)