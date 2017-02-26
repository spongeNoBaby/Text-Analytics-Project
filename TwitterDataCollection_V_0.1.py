# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 14:25:31 2017

@author: Mandi_V_0.0
"""

import tweepy
#import json
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = "SjXWPqhrbAJaWDoivx79Qrk5O"
consumer_secret = "aqoxfEEFmoFvYR1VluK2IIxeAIVD4qGoQMuqSjwtVq0fBWAOuc"
access_token = "2878937881-FnYV6i2ET6uB8fTIPtqomkij3q3k2xZ0BEgMNPj"
access_secret = "0wLwVzsVO6k0KbBYAl7Fj4lssYDfY9cupA3qOsWUU4gwA"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#==============================================================================
# for status in tweepy.Cursor(api.home_timeline).items(10):
#     print(status.text)
#     
# for friend in tweepy.Cursor(api.friends).items():
#     print(json.dumps(friend._json))
# 
# for tweet in tweepy.Cursor(api.user_timeline).items():
#     print(tweet.text)
#==============================================================================

class SamsungListener(StreamListener):
    def on_data(self, data):
        try:
            with open('Samsung.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s;" % str(e))
            return True
    
    def on_error(self, status):
        print(status)
        return True
    
twitter_stream = Stream(auth, SamsungListener())
twitter_stream.filter(track=['#Samsung'])