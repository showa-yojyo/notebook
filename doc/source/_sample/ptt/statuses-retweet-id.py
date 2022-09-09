#!/usr/bin/env python

# Demonstration POST statuses/retweet/:id
# See https://dev.twitter.com/rest/reference/post/statuses/retweet/%3Aid

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.statuses.retweet._id(
    _id=678987432331632643,
    trim_user=True,)

dump(response, sys.stdout, ensure_ascii=False, indent=4, sort_keys=True)
