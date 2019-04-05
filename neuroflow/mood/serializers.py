from mood.models import mood
from rest_framework import serializers
from django.utils import timezone

class MoodSerializer(object):
    def __init__(self, mood,created=None):
        self.mood = mood
        self.created = timezone.now()
