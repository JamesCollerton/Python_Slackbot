from SlackBot import SlackBot
from Twitter import Twitter
from NeuralNetwork import NeuralNetwork


def getDaveTweet():

    twitter = Twitter();
    return twitter.getDaveTweet();

def runNeuralNetwork():

    neuralNetwork = NeuralNetwork();
    neuralNetwork.runNeuralNetwork();

def main():

    # print(getDaveTweet())
    runNeuralNetwork();
    slackbot = SlackBot()
    slackbot.run()

if __name__ == "__main__":
    main()
