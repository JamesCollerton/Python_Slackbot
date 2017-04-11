import os
import time
import threading
import requests
import shutil

import Keys
from slackclient import SlackClient

class SlackBot:

    # Constants
    AT_BOT = "<@" + Keys.slack_bot_ID + ">"

    # Instantiate Slack & Twilio clients
    slack_client = SlackClient(Keys.slack_bot_token)

    def run(self):
        """
        Connects SlackBot using supplied credentials and
        starts a thread looking for input every one second.
        """
        if SlackBot.slack_client.rtm_connect():
            print("StarterBot connected and running!")
            threading.Timer(1, self.monitor).start()
        else:
            print("Connection failed. Invalid Slack token or bot ID?")

    def monitor(self):
        """
        Gets the command and channel from any input found from the
        slack channel and then passes it to the function which deals
        with it.
        """
        url, channel = self.parse_slack_output(SlackBot.slack_client.rtm_read())
        if url and channel:
            self.getImage(url)
            self.handle_command(url, channel)

        threading.Timer(1, self.monitor).start()

    def handle_command(self, command, channel):
        """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
        """

        attachments = [{"title": "Incredible, unique, Dave art",
                        "image_url": "http://cdn77.sadanduseless.com/wp-content/uploads/2016/05/potoo1.jpg"}];
        SlackBot.slack_client.api_call("chat.postMessage", channel=channel,
                                        as_user=True, attachments = attachments);


    def parse_slack_output(self, slack_rtm_output):
        """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
        """
        output_list = slack_rtm_output
        if output_list and len(output_list) > 0:
            for output in output_list:
                try:
                    url = output['file']['url_private']
                    channel = output['channel']
                    return url, channel
                except KeyError:
                    return None, None
        return None, None

    def getImage(self, url):
        """
        This takes in a URL from the slack message which corresponds
        to the location of the picture. It then downloads it.
        """
        token = Keys.slack_bot_token;
        path='images_input_temp/image_' + time.strftime("%c").replace(" ", "").replace(":","") + '.jpg'

        r = requests.get(url, stream=True, headers={'Authorization': 'Bearer %s' % token})
        if r.status_code == 200:
            with open(path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
