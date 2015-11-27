#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET lists/members
# https://dev.twitter.com/rest/reference/get/lists/members

from secret import twitter_instance

OWNER_SCREEN_NAME='showa_yojyo'
SLUG='informative'

tw = twitter_instance()

next_cursor = -1
while next_cursor != 0:
    response = tw.lists.members(
        owner_screen_name=OWNER_SCREEN_NAME,
        slug=SLUG,
        cursor=next_cursor)

    users = response['users']
    for i in users:
        print('{screen_name}:{description}'.format(**i).replace('\n', '\\n'))

    next_cursor = response['next_cursor']
