from app.src.reader import scrapper
from time import sleep

MINUTE = 60


class Twitter:
    def __init__(self, auth, params):
        self.auth = auth
        self.twitter = scrapper.TwitterScraper(params.account, auth.get_bearer_token())

    def set_monitor_account(self, account):
        self.twitter = scrapper.TwitterScraper(account, self.auth.get_bearer_token())

    def print_tweets(self, tweets):
        for tweet in tweets:
            print("-" * 20)
            print(f"{tweet['created_at']}-{tweet['text']}")

    def get_all_tweets(self):
        return self.twitter.get_all_tweets()

    def run(self):
        tweets = self.twitter.get_init_tweets()
        self.print_tweets(tweets[:min(5, len(tweets))][::-1])
        while True:
            sleep(MINUTE * 10)
            new_tweets = self.twitter.get_new_tweets()
            self.print_tweets(new_tweets)
