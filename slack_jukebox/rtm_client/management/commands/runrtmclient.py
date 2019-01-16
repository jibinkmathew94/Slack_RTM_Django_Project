from slackclient import SlackClient
import time
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Starts the rtm_client for the first'

    def handle(self, *args, **options):
        slack_token = "xoxb-521884446273-524058929266-NiaAvjKjd0uDQm18StLjTFbS"
        sc = SlackClient(slack_token)

        # sc.rtm_connect()

        # chakka = sc.rtm_read()
        # sc.rtm_send_message("video-upvoting", "sadakku mele")
        if sc.rtm_connect():
            for channel in sc.server.channels:
                if channel.name == "video-upvoting":
                    channel_id = channel.id
            print(channel_id)
            while True:
                message = sc.rtm_read()
                if message:
                    # sc.rtm_send_message("random", "test")
                    print(message)
                time.sleep(1)
        else:
            print("Connection Failed, invalid token?")
