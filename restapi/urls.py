from django.urls import path,include
from rest_framework import routers

from .views import UserViewSet, QuestionViewSet, AnswerViewSet
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'questions', QuestionViewSet)
# router.register(r'answers', AnswerViewSet)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]