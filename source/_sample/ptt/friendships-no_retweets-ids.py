#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET friendships/no_retweets/ids
# See https://dev.twitter.com/rest/reference/get/friendships/no_retweets/ids

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.friendships.no_retweets.ids()

dump(response, sys.stdout, ensure_ascii=False, indent=4)
