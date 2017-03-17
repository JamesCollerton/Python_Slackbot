import os
import time
import Keys

from slackclient import SlackClient

class SlackBot:

    # Constants
    AT_BOT = "<@" + Keys.slack_bot_ID + ">"

    # Instantiate Slack & Twilio clients
    slack_client = SlackClient(Keys.slack_bot_token)

    def run(self):
        """
        Connects SlackBot using supplied credentials
        """
        READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
        if SlackBot.slack_client.rtm_connect():
            print("StarterBot connected and running!")
            while True:
                command, channel = self.parse_slack_output(SlackBot.slack_client.rtm_read())
                if command and channel:
                    self.handle_command(command, channel)
                time.sleep(READ_WEBSOCKET_DELAY)
        else:
            print("Connection failed. Invalid Slack token or bot ID?")


    def handle_command(self, command, channel):
        """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
        """
        response = "len = " + str(len(command))
        SlackBot.slack_client.api_call("chat.postMessage", channel=channel,
                              text=response, as_user=True)


    def parse_slack_output(self, slack_rtm_output):
        """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
        """
        output_list = slack_rtm_output
        if output_list and len(output_list) > 0:
            for output in output_list:
                if output and 'text' in output and SlackBot.AT_BOT in output['text']:
                    # return text after the @ mention, whitespace removed
                    return output['text'].split(SlackBot.AT_BOT)[1].strip().lower(), \
                           output['channel']
        return None, None
