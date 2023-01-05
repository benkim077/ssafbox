from django.urls import include, path
from rest_framework import routers

from reviews import views

app_name = 'reviews'

router = routers.SimpleRouter()
router.register(r'reviews', views.ReviewViewSet, basename='reviews')

urlpatterns = [
    path('', include(router.urls)),
]