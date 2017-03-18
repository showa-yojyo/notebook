#!/usr/bin/env python

# Demonstration GET trends/closest
# See https://dev.twitter.com/rest/reference/get/trends/closest

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.trends.closest(long=139.773828, lat=35.696805)

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4, sort_keys=True)
