import datetime

from rest_framework import serializers

from screens.models import Theater, Screen, ScreenSchedule, ScreenSeat
from ssafbox.utils import SEAT_OCCUPY_TIME_LIMIT


class TheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theater
        fields = ('id', 'name', 'location')


class ScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screen
        fields = ('id', 'seats')


class ScreenScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenSchedule
        fields = ('id', 'start_date', 'start_time', 'movie', 'screen')
        read_only_fields = ('screen',)


class ScreenSeatSerializer(serializers.ModelSerializer):
    is_possible_to_reserve = serializers.SerializerMethodField()

    class Meta:
        model = ScreenSeat
        fields = ('id', 'schedule', 'is_reserved', 'seat_no', 'last_updated', 'is_possible_to_reserve')

    def get_is_possible_to_reserve(self, obj):
        duration = datetime.datetime.now(datetime.timezone.utc) - obj.last_updated
        if not obj.user:
            return True
        elif not obj.is_reserved and duration.total_seconds() > SEAT_OCCUPY_TIME_LIMIT:
            return True
        return False
