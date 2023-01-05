import datetime
import time

from django.db import transaction, DatabaseError
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.models import Movie
from movies.serializers import MovieSerializer
from screens.models import Theater, Screen, ScreenSchedule, ScreenSeat
from screens.serializers import TheaterSerializer, ScreenSerializer, ScreenScheduleSerializer, ScreenSeatSerializer
from ssafbox.permissions import IsAdminOrReadOnly
from ssafbox.utils import SEAT_OCCUPY_TIME_LIMIT


class TheaterViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminOrReadOnly]
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer


class ScreenViewSet(viewsets.ModelViewSet):
    queryset = Screen.objects.all()
    serializer_class = ScreenSerializer

    def get_queryset(self, *args, **kwargs):
        theater_id = self.kwargs.get('theater_pk')
        theater = Theater.objects.get(id=theater_id)
        if theater_id:
            queryset = self.queryset.filter(theater=theater)
        else:
            queryset = self.queryset
        return queryset

    def create(self, request, *args, **kwargs):
        theater_id = self.kwargs.get('theater_pk')
        theater = Theater.objects.get(id=theater_id)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(theater=theater)
            return Response(serializer.data)


class ScreenScheduleViewSet(viewsets.ModelViewSet):
    queryset = ScreenSchedule.objects.all()
    serializer_class = ScreenScheduleSerializer

    def get_queryset(self):
        screen_id = self.kwargs.get('screen_pk')
        screen = Screen.objects.get(id=screen_id)
        queryset = self.queryset.filter(screen=screen)
        return queryset

    def create(self, request, *args, **kwargs):
        screen_id = self.kwargs.get('screen_pk')
        screen = Screen.objects.get(id=screen_id)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            schedule = serializer.save(screen=screen)
            seats = [ScreenSeat(schedule=schedule, seat_no=i) for i in range(1, screen.seats + 1)]
            ScreenSeat.objects.bulk_create(seats)
            return Response(serializer.data)


class SeatOccupyAPI(APIView):
    def post(self, request, *args, **kwargs):
        seats_id = self.kwargs.get('id')

        try:
            with transaction.atomic():
                seats = ScreenSeat.objects.select_for_update(nowait=True) \
                    .filter(id=seats_id)

                for seat in seats:
                    duration = datetime.datetime.now(datetime.timezone.utc) - seat.last_updated

                    if not seat.user:
                        seat.user = request.user
                        seat.save()
                        return Response({'message': 'success'})
                    if not seat.is_reserved and duration.total_seconds() > SEAT_OCCUPY_TIME_LIMIT:
                        seat.user = request.user
                        seat.save()
                        return Response({'message': 'success'})
                    else:
                        # 불가능
                        return Response({'message': 'fail'})

        except DatabaseError:
            return Response({'message': 'fail'})


class SeatReserveAPI(APIView):
    def post(self, request, *args, **kwargs):
        schedule_id = self.kwargs.get('id')
        seat_no = request.data.get('seat_no')
        schedule = ScreenSchedule.objects.get(id=schedule_id)
        seat = ScreenSeat.objects.get(schedule=schedule, seat_no=seat_no)
        duration = datetime.datetime.now(datetime.timezone.utc) - seat.last_updated
        if seat.user == request.user and duration.total_seconds() < SEAT_OCCUPY_TIME_LIMIT:
            seat.is_reserved = True
            seat.save()
            return Response({'message': 'success'})
        else:
            return Response({'message': 'fail'})


class UserTheaterAPI(APIView):
    def get(self, request, *args, **kwargs):
        theaters = Theater.objects.all()
        serializer = TheaterSerializer(theaters, many=True)
        return Response(serializer.data)


class UserTheaterDateAPI(APIView):
    def get(self, request, *args, **kwargs):
        theater_id = self.kwargs.get('theater_pk')
        theater = Theater.objects.get(id=theater_id)
        screens = Screen.objects.filter(theater=theater)
        schedules = ScreenSchedule.objects.distinct('start_date').filter(screen__in=screens)
        dates = [schedule.start_date for schedule in schedules]
        return Response({'dates': dates})


class UserTheaterDateMovieAPI(APIView):
    def get(self, request, *args, **kwargs):
        theater_id = self.kwargs.get('theater_pk')
        theater = Theater.objects.get(id=theater_id)
        date = self.kwargs.get('date')

        screens = Screen.objects.filter(theater=theater)
        schedules = ScreenSchedule.objects. \
            select_related('movie'). \
            distinct('movie'). \
            filter(screen__in=screens, start_date=date)
        movies = [schedule.movie for schedule in schedules]

        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


class UserTheaterDateMovieScheduleAPI(APIView):
    def get(self, request, *args, **kwargs):
        theater_id = self.kwargs.get('theater_pk')
        theater = Theater.objects.get(id=theater_id)
        date = self.kwargs.get('date')
        movie_id = self.kwargs.get('movie_pk')
        movie = Movie.objects.get(id=movie_id)
        screens = Screen.objects.filter(theater=theater)
        schedules = ScreenSchedule.objects.filter(screen__in=screens, start_date=date, movie=movie)
        serializer = ScreenScheduleSerializer(schedules, many=True)
        return Response(serializer.data)


class UserScheduleAllSeatsAPI(APIView):
    def get(self, request, *args, **kwargs):
        schedule_id = self.kwargs.get('id')
        schedule = ScreenSchedule.objects.get(id=schedule_id)
        seats = ScreenSeat.objects.filter(schedule=schedule).order_by('seat_no')
        serializer = ScreenSeatSerializer(seats, many=True)
        return Response(serializer.data)
