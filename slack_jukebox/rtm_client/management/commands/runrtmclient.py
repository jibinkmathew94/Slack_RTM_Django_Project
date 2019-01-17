from slackclient import SlackClient
import time
from django.core.management.base import BaseCommand
from video_upvote.models import YoutubeVideo
import re


class Command(BaseCommand):
    help = 'Starts the rtm_client for the first'

    def handle(self, *args, **options):
        slack_token = "xoxb-521884446273-524058929266-NiaAvjKjd0uDQm18StLjTFbS"
        sc = SlackClient(slack_token)

        # sc.rtm_connect()

        # chakka = sc.rtm_read()
        # sc.rtm_send_rtm_data("video-upvoting", "sadakku mele")
        if sc.rtm_connect():
            for channel in sc.server.channels:
                if channel.name == "video-upvoting":
                    channel_id = channel.id
            print(channel_id)
            while True:
                rtm_data = sc.rtm_read()
                if rtm_data:
                    if 'message' in rtm_data[0]:
                        message = rtm_data[0]['message']
                        text_message = message['text']
                        link_match = re.search("youtube.com/watch\\?v=[a-zA-Z0-9_-]{11}", text_message)
                        if link_match:
                            youtube_video_id = re.findall("[a-zA-Z0-9_-]{11}", link_match.group())[0]
                            youtubelink = YoutubeVideo(video_id=youtube_video_id)
                            if 'attachments' in message:
                                attachments = message['attachments'][0]
                                youtubelink.thumbnail_url = attachments['thumb_url']
                                print(attachments['title'])
                                youtubelink.title = attachments['title']
                                print(attachments['thumb_url'])
                            youtubelink.save()
                    # 
                    # sc.rtm_send_rtm_data("random", "test")
                time.sleep(1)
        else:
            print("Connection Failed, invalid token?")

# elif(rtm_data[0]['type'] == 'message'):
#                         link_match = re.search("youtube.com/watch\\?v=[a-zA-Z0-9_-]{11}", rtm_data[0]['text'])
#                         if link_match:
#                             youtube_link = re.findall("[a-zA-Z0-9_-]{11}", link_match.group())[0]
#                             youtubelink = YoutubeVideo(link=youtube_link)
#                             youtubelink.save()