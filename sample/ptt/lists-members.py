# -*- coding: utf-8 -*-

# Demonstration GET lists/members
# https://dev.twitter.com/docs/api/1.1/get/lists/members

from twitter import *
from secret import twitter_instance

tw = twitter_instance()

OWNER_SCREEN_NAME='showa_yojyo'
SLUG='news'

# GET lists/members
response = tw.lists.members(
    owner_screen_name=OWNER_SCREEN_NAME,
    slug=SLUG)

screen_names = [user['screen_name'] for user in response['users']]

while response['next_cursor'] != 0:
    response = tw.lists.members(
        owner_screen_name=OWNER_SCREEN_NAME,
        slug=SLUG,
        cursor=response['next_cursor'])

    screen_names.extend([user['screen_name'] for user in response['users']])

for screen_name in screen_names:
    print(screen_name)
