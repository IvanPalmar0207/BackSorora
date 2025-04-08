from django.urls import path, include
from rest_framework import routers
from .views import NoteView

routerNote = routers.DefaultRouter()
routerNote.register(r'note', NoteView, basename='note')

urlpatterns = [
    path('note/', include(routerNote.urls))
]