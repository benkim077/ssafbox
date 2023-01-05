from django.contrib.auth import get_user_model
from rest_framework import serializers

from movies.models import Movie
from orders.serializers import OrderSerializer
from screens.models import ScreenSeat
from screens.serializers import ScreenScheduleSerializer


class CustomUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'is_staff', 'username', 'last_login')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'running_time')


class ScheduleSerializer(ScreenScheduleSerializer):
    movie = MovieSerializer(read_only=True)


class UserReservedInfoSerializer(serializers.ModelSerializer):
    order_set = OrderSerializer(many=True)
    schedule = ScheduleSerializer()

    class Meta:
        model = ScreenSeat
        fields = ('order_set', 'seat_no', 'schedule')
