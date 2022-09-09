#!/usr/bin/env python

# Demonstration GET favorites
# See https://dev.twitter.com/rest/reference/get/favorites/list

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.favorites.list(
    screen_name='showa_yojyo',
    count=1,
    include_entities=False)

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4, sort_keys=True)
