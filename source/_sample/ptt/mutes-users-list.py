#!/usr/bin/env python

# Demonstration GET mutes/users/list
# See https://dev.twitter.com/rest/reference/get/mutes/users/list

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.mutes.users.list()

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4, sort_keys=True)
