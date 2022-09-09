#!/usr/bin/env python

# Demonstration POST statuses/destroy/:id
# See https://dev.twitter.com/rest/reference/post/statuses/destroy/%3Aid

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.statuses.destroy._id(
    _id=679306282629619712,
    trim_user=True,)

dump(response, sys.stdout, ensure_ascii=False, indent=4, sort_keys=True)
