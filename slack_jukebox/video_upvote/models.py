from django.conf import settings
from django.db import models

# Create your models here.

User = settings.AUTH_USER_MODEL


class YoutubeVideo(models.Model):
    video_id = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail_url = models.CharField(max_length=120, blank=True)
    title = models.CharField(max_length=120, blank=True)
    upvotes = models.ManyToManyField(User, related_name='upvoted')

    def __str__(self):
        return self.title