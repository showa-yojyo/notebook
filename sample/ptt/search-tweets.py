# -*- coding: utf-8 -*-

# Demonstration GET search/tweets
# See https://dev.twitter.com/docs/api/1.1/get/search/tweets

from twitter import *
from secret import twitter_instance

tw = twitter_instance()

# Comment 1
response = tw.search.tweets(
    q='ネシカ OR nesica',
    rpp=33)

# Comment 2
for result in response['statuses']:
    print('{created_at} {user[screen_name]} {text}'.format(**result))
