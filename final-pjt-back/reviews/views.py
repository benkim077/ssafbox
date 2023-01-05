from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status

from movies.models import Movie
from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        movie_id = self.request.GET.get('movie_id')
        movie = Movie.objects.get(id=movie_id)
        queryset = self.queryset.filter(movie=movie)
        return queryset

    def create(self, request, *args, **kwargs):
        movie_id = self.request.data.get('movie_id')
        movie = Movie.objects.get(id=movie_id)
        data = {
            'movie': movie.id,
            'user': request.user.id,
            'content': request.data.get('content')
        }
        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def list(self, request, *args, **kwargs):
        movie_id = request.GET.get('movie_id')
        movie = Movie.objects.get(id=movie_id)
        queryset = self.queryset.filter(movie=movie)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):

        review_id = self.kwargs.get('pk')
        review = Review.objects.get(id=review_id)
        if request.user != review.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(review)
        return Response(status=status.HTTP_204_NO_CONTENT)
