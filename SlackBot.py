import os
import time
import threading

import Keys
from slackclient import SlackClient

class SlackBot:

    # Constants
    AT_BOT = "<@" + Keys.slack_bot_ID + ">"

    # Instantiate Slack & Twilio clients
    slack_client = SlackClient(Keys.slack_bot_token)

    # Create thread for running SlackBot monitor

    def run(self):
        """
        Connects SlackBot using supplied credentials and
        starts a thread looking for input every one second
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
        print("Hello")
        command, channel = self.parse_slack_output(SlackBot.slack_client.rtm_read())
        if command and channel:
            self.handle_command(command, channel)

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
                print(output)
                if output and 'text' in output and SlackBot.AT_BOT in output['text']:
                    # return text after the @ mention, whitespace removed
                    return output['text'].split(SlackBot.AT_BOT)[1].strip().lower(), \
                           output['channel']
        return None, None
