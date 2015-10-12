#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET lists/subscribers
# https://dev.twitter.com/rest/reference/get/lists/subscribers

from secret import twitter_instance

tw = twitter_instance()

response = tw.lists.subscribers(
    owner_screen_name='showa_yojyo',
    slug='informative',
    count=20,
    cursor=-1)

for item in response['users']:
    print('{screen_name}: {description}'.format(**item))
