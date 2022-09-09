#!/usr/bin/env python

# Demonstration GET statuses/retweets/:id
# See https://dev.twitter.com/rest/reference/get/statuses/retweets/%3Aid

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.statuses.retweets._id(
    _id=653256646810955776,
    trim_user=True,)

dump(response, sys.stdout, ensure_ascii=False, indent=4, sort_keys=True)
