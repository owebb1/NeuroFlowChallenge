from django.shortcuts import render
from mood.models import mood
from mood.serializers import MoodSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

class MoodList(ViewSet):
    queryset = mood.objects.all()
    serializer_class = MoodSerializer(queryset)

    def post(self, request, format=None):
        mood = MoodSerializer(data=request.data)
        if mood.is_valid():
            mood.save()
            return Response(mood.data, status=status.HTTP_201_CREATED)
        return Response(mood.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        mood = mood.objects.all()
        serializer = MoodSerializer(username, many=True)
        return Response(serializer.data)

#class User(ViewSet):
