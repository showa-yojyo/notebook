#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET lists/subscriptions
# https://dev.twitter.com/rest/reference/get/lists/subscriptions

from secret import twitter_instance

tw = twitter_instance()

response = tw.lists.subscriptions(
    screen_name='showa_yojyo', 
    count=20,
    cursor=-1)

for item in response['lists']:
    print('{full_name}: {description}'.format(**item))
