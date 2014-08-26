#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET statuses/retweets_of_me
# See https://dev.twitter.com/docs/api/1.1/get/statuses/retweets_of_me

from secret import twitter_instance

tw = twitter_instance()
stats = tw.statuses.retweets_of_me(
    screen_name='showa_yojyo',
    count=20)

# https://dev.twitter.com/docs/api/1.1/get/statuses/retweets:id
# https://dev.twitter.com/docs/api/1.1/get/statuses/retweeters/ids
for stat in stats:
    #user = stat['user']
    print('''
{user[screen_name]} / {user[name]} ({created_at}) [{source}]
{text}
retweeted: {retweet_count}
'''.format(**stat))
