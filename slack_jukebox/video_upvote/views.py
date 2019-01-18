from django.shortcuts import render
from django.views.generic import ListView
from .models import YoutubeVideo
from django.http import JsonResponse
import json
from django.db.models import Count
# Create your views here.


class HomeView(ListView):
    model = YoutubeVideo
    template_name = "video_upvote/home.html"
    context_object_name = 'videos'
    queryset = YoutubeVideo.objects.annotate(num_upvotes=Count('upvotes')).order_by('-num_upvotes')


def upvote(request):
    if request.user.is_authenticated:
        video_id = json.loads(request.body)['data']  # get video id 
        up_or_down = json.loads(request.body)['vote']
        youtube_video = YoutubeVideo.objects.filter(video_id=video_id)[0]
        if youtube_video:
            if up_or_down == "up":
                youtube_video.upvotes.add(request.user)  # add vote
                return JsonResponse({'data':'vote added'})
            elif up_or_down == "down":
                if request.user in youtube_video.upvotes.all():  #undo last vote
                    youtube_video.upvotes.remove(request.user)
                return JsonResponse({'data':'vote removed'})
            youtube_video.save()
        else:
            return JsonResponse({'data':'no video'})
    else:
        return JsonResponse({'data':'invalid login'})
    
