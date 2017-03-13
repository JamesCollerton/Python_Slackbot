from Twitter import Twitter

def getDaveTweet():

    twitter = Twitter();
    return twitter.getDaveTweet();

def main():

    print(getDaveTweet());

if __name__ == "__main__":
    main()
