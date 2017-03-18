#!/usr/bin/env python

# Demonstration GET trends/place
# See https://dev.twitter.com/rest/reference/get/trends/place

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.trends.place(_id=23424856)

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4, sort_keys=True)
