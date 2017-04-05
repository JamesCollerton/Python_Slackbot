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
        # self.getImage();

    def monitor(self):
        """
        Gets the command and channel from any input found from the
        slack channel and then passes it to the function which deals
        with it.
        """
        # command, channel = self.parse_slack_output(SlackBot.slack_client.rtm_read())
        # if command and channel:
        #     self.handle_command(command, channel)
        #
        # threading.Timer(1, self.monitor).start()
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
        # output_list = slack_rtm_output
        # if output_list and len(output_list) > 0:
        #     for output in output_list:
        #         if output and 'text' in output and SlackBot.AT_BOT in output['text']:
        #             # return text after the @ mention, whitespace removed
        #             return output['text'].split(SlackBot.AT_BOT)[1].strip().lower(), \
        #                    output['channel']
        # return None, None

        output_list = slack_rtm_output
        if output_list and len(output_list) > 0:
            for output in output_list:
                # print('')
                # print(output)
                # print('')
                try:
                    url = output['file']['url_private']
                    channel = output['channel']
                    return url, channel
                except KeyError:
                    return None, None

                # if (output and 'file' in output) and (output['file'] and output['file']['url_private'] in output['file']):
                #     return output['file']['url_private'], \
                #            output['channel']
                # elif output and 'text' in output and SlackBot.AT_BOT in output['text']:
                #     return output['text'].split(SlackBot.AT_BOT)[1].strip().lower(), \
                #            output['channel']
        # return None, None

    # def parse_slack_file_output(self, slack_rtm_output):
    #     """
    #     The Slack Real Time Messaging API is an events firehose.
    #     this parsing function returns None unless a message is
    #     directed at the Bot, based on its ID.
    #     """
    #     output_list = slack_rtm_output
    #     if output_list and len(output_list) > 0:
    #         for output in output_list:
    #             if output and 'url_private' in output and SlackBot.AT_BOT in output['text']:
    #                 # return text after the @ mention, whitespace removed
    #                 return output['text'].split(SlackBot.AT_BOT)[1].strip().lower(), \
    #                        output['channel']
    #     return None, None

    def getImage(self, url):
        # url = 'https://files.slack.com/files-pri/T4F8BB072-F4TGMV54J/donelli.jpg';
        token = Keys.slack_bot_token;
        path='test.jpg'

        r = requests.get(url, stream=True, headers={'Authorization': 'Bearer %s' % token})
        if r.status_code == 200:
            with open(path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
