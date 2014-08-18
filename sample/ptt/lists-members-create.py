# -*- coding: utf-8 -*-

# Demonstration POST lists/members/create
# https://dev.twitter.com/docs/api/1.1/post/lists/members/create

from twitter import *
from secret import twitter_instance

tw = twitter_instance()

tw.lists.members.create(
    owner_screen_name='showa_yojyo',
    slug='listname',
    screen_name=screen_name) # デモコードなので自分自身決め打ち
