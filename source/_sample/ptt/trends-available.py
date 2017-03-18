#!/usr/bin/env python

# Demonstration GET trends/available
# See https://dev.twitter.com/rest/reference/get/trends/available

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.trends.available()

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4, sort_keys=True)
