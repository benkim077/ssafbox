import random
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.models import Movie
from movies.serializers import MovieSerializer


class MoviePageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MoviePageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset = self.queryset
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class MovieRecommendationAPI(APIView):
    def get(self, request, *args, **kwargs):
        movie = random.choice(Movie.objects.order_by('-score')[:100])
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
