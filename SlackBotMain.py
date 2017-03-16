from SlackBot import SlackBot
from Twitter import Twitter


def getDaveTweet():

    twitter = Twitter();
    return twitter.getDaveTweet();


def main():

    # print(getDaveTweet())

    slackbot = SlackBot()
    slackbot.run()


if __name__ == "__main__":
    main()
