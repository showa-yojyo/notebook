#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET lists/subscriptions
# https://dev.twitter.com/rest/reference/get/lists/subscriptions

from secret import twitter_instance

tw = twitter_instance()

next_cursor = -1
while next_cursor:
    response = tw.lists.subscriptions(
        screen_name='showa_yojyo', 
        cursor=next_cursor)

    for item in response['lists']:
        print('{full_name}: {description}'.format(**item).replace('\n', '\\n'))

    next_cursor = response['next_cursor']
