#!/usr/bin/env python

# Demonstration GET accout/settings
# https://dev.twitter.com/rest/reference/get/account/settings

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.account.settings(_method='GET')

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4, sort_keys=True)
