#!/usr/bin/env python

# Demonstration POST mutes/users/create
# See https://dev.twitter.com/rest/reference/post/mutes/users/create

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.mutes.users.create(screen_name='showa_yojyo')

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4, sort_keys=True)
