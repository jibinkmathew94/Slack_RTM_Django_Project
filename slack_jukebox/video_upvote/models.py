from django.conf import settings
from django.db import models

# Create your models here.

User = settings.AUTH_USER_MODEL


class YoutubeVideo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(User, related_name='upvoted')

    def __str__(self):
        return self.name
