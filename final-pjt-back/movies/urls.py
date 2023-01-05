from django.urls import path, include
from rest_framework import routers

from movies import views

app_name = 'movies'

router = routers.SimpleRouter()
router.register(r'movies', views.MovieViewSet, basename='movies')

urlpatterns = [
    path('', include(router.urls)),
    path('recommendation/', views.MovieRecommendationAPI.as_view(), name='recommendation'),
]