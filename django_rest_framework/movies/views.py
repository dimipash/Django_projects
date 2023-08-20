from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieData


class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all().order_by('name')
    serializer_class = MovieSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='action').order_by('name')
    serializer_class = MovieSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='comedy').order_by('name')
    serializer_class = MovieSerializer
