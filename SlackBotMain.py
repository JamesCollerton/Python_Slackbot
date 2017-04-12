from SlackBot import SlackBot
from Twitter import Twitter
from NeuralNetwork import NeuralNetwork
from ImageQueue import ImageQueue

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

def runQueue():

    imageQueue = ImageQueue();
    imageQueue.run();

def main():

    # print(getDaveTweet())
    # runNeuralNetwork('1-style.jpg');
    # runSlackBot();
    runQueue();

if __name__ == "__main__":
    main()
