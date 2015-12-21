#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration POST friendships/update
# See https://dev.twitter.com/rest/reference/post/friendships/update

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.friendships.update(
    screen_name='showa_yojyo',
    device=True,
    retweets=True,)

dump(response, sys.stdout, ensure_ascii=False, indent=4)
