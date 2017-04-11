from SlackBot import SlackBot
from Twitter import Twitter
from NeuralNetwork import NeuralNetwork

import sys
import signal

def getDaveTweet():

    twitter = Twitter();
    return twitter.getDaveTweet();

def runNeuralNetwork(imageName):

    neuralNetwork = NeuralNetwork();
    neuralNetwork.runNeuralNetwork(imageName);

def runSlackBot():

    slackbot = SlackBot();
    slackbot.run();

def main():

    # print(getDaveTweet())
    # runNeuralNetwork('1-style.jpg');
    runSlackBot();

if __name__ == "__main__":
    main()
