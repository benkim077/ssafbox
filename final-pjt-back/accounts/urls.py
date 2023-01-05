from django.contrib import admin
from django.urls import path, include
from accounts import views

app_name = 'accounts'

urlpatterns = [
    # path('google/login/', views.google_login, name='google_login'),
    # path('google/callback/', views.google_callback, name='google_callback'),
    # path('google/login/finish/', views.GoogleLogin.as_view(), name='google_login_todjango'),
    path('user-reserved-seats/', views.UserOrdersView.as_view(), name='user_reserved_seats'),
]
