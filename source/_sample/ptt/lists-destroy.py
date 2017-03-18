#!/usr/bin/env python

# Demonstration POST lists/destroy
# https://dev.twitter.com/rest/reference/post/lists/destroy
from secret import twitter_instance

tw = twitter_instance()
tw.lists.destroy(
    owner_screen_name='showa_yojyo',
    slug='listname',)
