#!/usr/bin/env python

# Demonstration POST statuses/unretweet/:id
# See https://dev.twitter.com/rest/reference/post/statuses/unretweet/%3Aid

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.statuses.unretweet._id(
    _id=708317138675630082,
    trim_user=True,)

dump(response, sys.stdout, ensure_ascii=False, indent=4, sort_keys=True)
