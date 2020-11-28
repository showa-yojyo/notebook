#!/usr/bin/env python

# Demonstration POST friendships/create
# See https://dev.twitter.com/rest/reference/post/friendships/create

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.friendships.create(
    screen_name='showa_yojyo',
    follow=True)

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4, sort_keys=True)
