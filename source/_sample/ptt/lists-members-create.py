#!/usr/bin/env python

# Demonstration POST lists/members/create
# https://dev.twitter.com/rest/reference/post/lists/members/create

from secret import twitter_instance

tw = twitter_instance()

tw.lists.members.create(
    owner_screen_name='showa_yojyo',
    slug='listname',
    screen_name=screen_name)
