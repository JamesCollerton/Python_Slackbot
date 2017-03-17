from SlackBot import SlackBot
from Twitter import Twitter
from NeuralNetwork import NeuralNetwork

def getDaveTweet():

    twitter = Twitter();
    return twitter.getDaveTweet();

def runNeuralNetwork():

    neuralNetwork = NeuralNetwork();
    neuralNetwork.runNeuralNetwork();

def runSlackBot():

    slackbot = SlackBot();
    slackbot.run();

def main():

    # print(getDaveTweet())
    # runNeuralNetwork();
    runSlackBot();

if __name__ == "__main__":
    main()
