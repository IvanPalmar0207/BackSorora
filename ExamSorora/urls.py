from django.urls import path, include
from rest_framework import routers
from .views import ExamViewSet, QuestionViewSet, ScoreViewSet, ActionViewSet

routerExam = routers.DefaultRouter()
routerExam.register(r'exam', ExamViewSet, basename = 'exam')

routerQuestion = routers.DefaultRouter()
routerQuestion.register(r'question', QuestionViewSet, basename = 'question')

routerScore = routers.DefaultRouter()
routerScore.register(r'score', ScoreViewSet, basename = 'Score')

routerAction = routers.DefaultRouter()
routerAction.register(r'action', ActionViewSet, basename = 'Action')

urlpatterns = [
    path('exam/', include(routerExam.urls)),
    path('question/', include(routerQuestion.urls)),
    path('score/', include(routerScore.urls)),
    path('action/', include(routerAction.urls))
]