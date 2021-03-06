#!/usr/bin/env python

# Demonstration POST favorites/create
# See https://dev.twitter.com/rest/reference/post/favorites/create

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.favorites.create(
    _id=653256646810955776,
    include_entities=False)

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4, sort_keys=True)
