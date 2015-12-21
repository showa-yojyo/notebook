#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET friendships/lookup
# See https://dev.twitter.com/rest/reference/get/friendships/lookup

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
ids = ','.join((str(i) for i in (577367985, 1220723053, 1288619659)))
response = tw.friendships.lookup(user_id=ids)

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4)
