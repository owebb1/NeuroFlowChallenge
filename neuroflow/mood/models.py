from django.db import models
from django.utils import timezone

class mood(models.Model):
    mood = models.CharField(max_length=100)
    created = timezone.now()

    def create_mood(cls, mood):
        mood = cls(mood=mood)
        return mood
