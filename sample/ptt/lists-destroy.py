# -*- coding: utf-8 -*-

# Demonstration POST lists/destroy
# https://dev.twitter.com/docs/api/1.1/post/lists/destroy
from twitter import *
from secret import twitter_instance

tw = twitter_instance()
tw.lists.destroy(
    owner_screen_name='showa_yojyo',
    slug='listname',)

