#!/usr/bin/env python3

import requests
from time import sleep

baseurl = 'https://api.twitter.com/1.1/search/tweets.json?q=(from%3A{account}) &src=typed_query&f=live'


class TwitterScraper:
    def __init__(self, account, auth):
        self.url = baseurl.format(**{"account": account})
        self.headers = {"Authorization": auth}
        self.seen_tweets = []

    def get_seen_ids(self):
        return set(map(lambda t: t['id'], self.seen_tweets))

    def add_seen(self, tweets):
        seen_ids = self.get_seen_ids()
        for tweet in tweets:
            if tweet['id'] not in seen_ids:
                self.seen_tweets.append(tweet)

    def get_all_tweets(self):
        return list(map(lambda t: {"created_at": t["created_at"], 'text': t['text']}, self.seen_tweets))

    def get_new_tweets(self):
        attempt = 5
        while attempt > 0:
            try:
                page = requests.get(self.url, headers=self.headers).json()
                if 'statuses' in page:
                    tweets = page['statuses']
                    existing_ids = set(map(lambda t: t['id'], self.seen_tweets))
                    new_tweets = [tweet for tweet in tweets if tweet['id'] not in existing_ids]
                    self.add_seen(tweets)
                    return [{"created_at": tweet["created_at"], 'text': tweet['text']} for tweet in new_tweets]
                else:
                    return []
            except KeyError:
                attempt -= 1
                sleep(5)
        raise (KeyError, f"api endpoint {self.url} is no longer returning meaningful results")

    def get_init_tweets(self):
        tweets = self.get_new_tweets()
        return tweets[:min(5, len(tweets))] if tweets else []
