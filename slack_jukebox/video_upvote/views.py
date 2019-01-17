from django.shortcuts import render
from django.views.generic import ListView
from .models import YoutubeVideo
# Create your views here.


class HomeView(ListView):
    model = YoutubeVideo
    template_name = "video_upvote/home.html"
    context_object_name = 'videos'

