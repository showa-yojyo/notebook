#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration POST friendships/destroy
# See https://dev.twitter.com/rest/reference/post/friendships/destroy

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.friendships.destroy(screen_name='showa_yojyo')

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4, sort_keys=True)
