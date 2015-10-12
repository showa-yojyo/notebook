#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET lists/members
# https://dev.twitter.com/rest/reference/get/lists/members

from secret import twitter_instance

OWNER_SCREEN_NAME='showa_yojyo'
SLUG='news'

tw = twitter_instance()
next_cursor = -1
screen_names = list()

while next_cursor != 0:
    # GET lists/members
    response = tw.lists.members(
        owner_screen_name=OWNER_SCREEN_NAME,
        cursor=next_cursor,
        slug=SLUG)

    screen_names.extend([user['screen_name'] for user in response['users']])

    next_cursor = response['next_cursor']

for screen_name in screen_names:
    print(screen_name)
