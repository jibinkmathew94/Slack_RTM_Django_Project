from slackclient import SlackClient
import time
from django.core.management.base import BaseCommand
from video_upvote.models import YoutubeVideo
import re
import os


class Command(BaseCommand):
    help = 'Starts the rtm_client for the first'

    def handle(self, *args, **options):
        slack_token = os.environ["SLACK_BOT_TOKEN"]  # bot token for rtm communication
        channel_name = os.environ["CHANNEL_NAME"]
        sc = SlackClient(slack_token)
        if sc.rtm_connect():
            for channel in sc.server.channels:  # searching for channel id with the given channel name
                if channel.name == channel_name:
                    channel_id = channel.id
            while True: # listening to websocket connection(rtm)
                rtm_data = sc.rtm_read()  
                if rtm_data:
                    if 'message' in rtm_data[0]:
                        message = rtm_data[0]['message']
                        text_message = message['text']
                        youtube_link = re.search("youtube.com/watch\\?v=[a-zA-Z0-9_-]{11}", text_message)   # extracting video id from the link
                        if youtube_link:   # checking for a valid youtube link
                            youtube_video_id = re.findall("[a-zA-Z0-9_-]{11}", youtube_link.group())[0] #extracting youtube video id
                            youtube_video = YoutubeVideo(video_id=youtube_video_id)
                            if 'attachments' in message:
                                attachments = message['attachments'][0]
                                youtube_video.thumbnail_url = attachments['thumb_url']
                                youtube_video.title = attachments['title']
                            youtube_video.save()
                time.sleep(1)
        else:
            print("Connection Failed, invalid token?")