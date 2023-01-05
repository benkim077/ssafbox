from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_nested import routers
from screens import views
from django.urls import path, include

app_name = 'screens'

theater_router = SimpleRouter()
theater_router.register('theaters', views.TheaterViewSet, basename='theaters')

screen_router = routers.NestedSimpleRouter(
    theater_router,
    r'theaters',
    lookup='theater',
)
screen_router.register(
    r'screens',
    views.ScreenViewSet,
    basename='screens'
)

screen_schedule_router = routers.NestedSimpleRouter(
    screen_router,
    r'screens',
    lookup='screen',
)
screen_schedule_router.register(
    r'schedules',
    views.ScreenScheduleViewSet,
    basename='schedules'
)
urlpatterns = [

]

mypatterns = [
    path('', include(screen_router.urls)),
    path('', include(screen_schedule_router.urls)),
    path('seats/<int:id>/occupy/', views.SeatOccupyAPI.as_view(), name='seat-occupy'),
    path('available_theaters/', views.UserTheaterAPI.as_view(), name='available_theaters'),
    path('available_date/<int:theater_pk>/', views.UserTheaterDateAPI.as_view(), name='available_schedules'),
    path('available_movie/<int:theater_pk>/<str:date>/', views.UserTheaterDateMovieAPI.as_view(),
         name='available_movie'),
    path('available_schedule/<int:theater_pk>/<str:date>/<int:movie_pk>/',
         views.UserTheaterDateMovieScheduleAPI.as_view(), name='available_schedule'),
    path('available_seats/<int:id>/', views.UserScheduleAllSeatsAPI.as_view(), name='available_seats'),
]
urlpatterns += theater_router.urls
urlpatterns += mypatterns
